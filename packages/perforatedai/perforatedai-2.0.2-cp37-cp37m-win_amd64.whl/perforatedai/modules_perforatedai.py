# Copyright (c) 2025 Perforated AI

import copy
import math
import os
import pdb
import sys
import time
from datetime import datetime

import numpy as np
import torch
import torch.nn as nn

from perforatedai import globals_perforatedai as GPA
from perforatedai import utils_perforatedai as UPA

try:
    from perforatedbp import modules_pbp as MPB
except Exception as e:
    pass


# Values for Dendrite training, minimally used in open source version
DENDRITE_TENSOR_VALUES = [
    "shape"
]  # Shape is tensor of same shape as total neurons in layer
DENDRITE_SINGLE_VALUES = []

DENDRITE_INIT_VALUES = ["initialized", "current_d_init"]


VALUE_TRACKER_ARRAYS = ["dendrite_outs"]
if GPA.pc.get_perforated_backpropagation():
    DENDRITE_TENSOR_VALUES = MPB.update_dendrite_tensor_values(DENDRITE_TENSOR_VALUES)
    DENDRITE_SINGLE_VALUES = MPB.update_dendrite_single_values(DENDRITE_SINGLE_VALUES)
    VALUE_TRACKER_ARRAYS = MPB.update_value_tracker_arrays(VALUE_TRACKER_ARRAYS)

# Values for reinitializing and saving dendrite scaffolding
DENDRITE_REINIT_VALUES = DENDRITE_TENSOR_VALUES + DENDRITE_SINGLE_VALUES
DENDRITE_SAVE_VALUES = (
    DENDRITE_TENSOR_VALUES + DENDRITE_SINGLE_VALUES + DENDRITE_INIT_VALUES
)


def filter_backward(grad_out, values, candidate_nonlinear_outs):
    """Filter backward pass for gradient processing.

    This function processes gradients during the backward pass,
    ensuring correct input dimensions,and applying perforated backpropagation if enabled.

    Parameters
    ----------
    grad_out : torch.Tensor
        The gradient output tensor from the backward pass.
    values : DendriteValueTracker
        A DendriteValueTracker instance containing values associated with the module being processed.
    candidate_nonlinear_outs : dict
        A dictionary of candidate modules outputs after non-linear activation.

    Returns
    -------
    None
    """
    if GPA.pc.get_extra_verbose():
        print(f"{values[0].layer_name} calling backward")

    with torch.no_grad():
        val = grad_out.detach()
        # If the input dimensions are not initialized
        if not values[0].current_d_init.item():
            # If input dimensions and gradient don't have same shape trigger error and quit
            if len(values[0].this_input_dimensions) != len(grad_out.shape):
                print("The following layer has not properly set this_input_dimensions")
                print(values[0].layer_name)
                print("it is expecting:")
                print(values[0].this_input_dimensions)
                print("but received")
                print(grad_out.shape)
                print(
                    "to check these all at once set GPA.pc.set_debugging_input_dimensions(1)"
                )
                print(
                    "Call set_this_input_dimensions on this layer after initialize_pai"
                )
                if not GPA.pc.get_debugging_input_dimensions():
                    sys.exit(0)
                else:
                    GPA.pc.set_debugging_input_dimensions(2)
                    return
            # Make sure that the input dimensions are correct
            for i in range(len(values[0].this_input_dimensions)):
                if values[0].this_input_dimensions[i] == 0:
                    continue
                # Make sure all input dimensions are either -1 (new format) or exact values (old format)
                if (
                    not (grad_out.shape[i] == values[0].this_input_dimensions[i])
                    and not values[0].this_input_dimensions[i] == -1
                ):
                    print(
                        "The following layer has not properly set this_input_dimensions with this incorrect shape"
                    )
                    print(values[0].layer_name)
                    print("it is expecting:")
                    print(values[0].this_input_dimensions)
                    print("but received")
                    print(grad_out.shape)
                    print(
                        "to check these all at once set GPA.pc.set_debugging_input_dimensions(1)"
                    )
                    if not GPA.pc.get_debugging_input_dimensions():
                        sys.exit(0)
                    else:
                        GPA.pc.set_debugging_input_dimensions(2)
                        return
            # Setup the arrays with the now known shape
            with torch.no_grad():
                if GPA.pc.get_verbose():
                    print("setting d shape for")
                    print(values[0].layer_name)
                    print(val.size())

                values[0].set_out_channels(val.size())
                values[0].setup_arrays(values[0].out_channels)
            # Flag that it has been setup
            values[0].current_d_init[0] = 1
        if GPA.pc.get_perforated_backpropagation():
            MPB.filter_backward_pb(val, values, candidate_nonlinear_outs)


def set_wrapped_params(model):
    """Set parameters as wrapped with dendrites.

    Parameters
    ----------
    model : torch.nn.Module
        The model whose parameters are to be marked as wrapped.

    Returns
    -------
    None

    """
    for param in model.parameters():
        param.wrapped = True


def set_tracked_params(model):
    """Set parameters as tracked without dendrites.

    Parameters
    ----------
    model : torch.nn.Module
        The model whose parameters are to be marked as tracked.

    Returns
    -------
    None
    """
    for param in model.parameters():
        param.tracked = True


class PAINeuronModule(nn.Module):
    """Wrapper to set a module as one that will have dendritic copies."""

    def __init__(self, start_module, name):
        """Initialize PAINeuronModule.

        This function sets up the neuron module to wrap the start_module
        and manage its dendritic connections.

        Parameters
        ----------
        start_module : nn.Module
            The module to wrap.
        name : str
            The name of the neuron module.
        """
        super(PAINeuronModule, self).__init__()

        self.main_module = start_module
        self.name = name

        set_wrapped_params(self.main_module)
        if GPA.pc.get_verbose():
            print(
                f"initing a layer {self.name} with main type {type(self.main_module)}"
            )
            print(start_module)

        # If this main_module is one that requires processing set the processor
        if type(self.main_module) in GPA.pc.get_modules_with_processing():
            module_index = GPA.pc.get_modules_with_processing().index(
                type(self.main_module)
            )
            self.processor = GPA.pc.get_modules_processing_classes()[module_index]()
            if GPA.pc.get_verbose():
                print("with processor")
                print(self.processor)
        elif (
            type(self.main_module).__name__ in GPA.pc.get_module_names_with_processing()
        ):
            module_index = GPA.pc.get_module_names_with_processing().index(
                type(self.main_module).__name__
            )
            self.processor = GPA.pc.get_module_by_name_processing_classes()[
                module_index
            ]()
            if GPA.pc.get_verbose():
                print("with processor")
                print(self.processor)
        else:
            self.processor = None

        # Field that can be filled in if your activation function requires a parameter
        self.activation_function_value = -1
        self.type = "neuron_module"

        self.register_buffer(
            "this_input_dimensions", (torch.tensor(GPA.pc.get_input_dimensions()))
        )
        if (self.this_input_dimensions == 0).sum() != 1:
            print(f"5 Need exactly one 0 in the input dimensions: {self.name}")
            print(self.this_input_dimensions)
            sys.exit(-1)
        self.register_buffer(
            "this_node_index", torch.tensor(GPA.pc.get_input_dimensions().index(0))
        )
        self.dendrite_modules_added = 0

        # Values for dendrite to neuron weights
        self.dendrites_to_top = nn.ParameterList()
        self.register_parameter("newest_dendrite_to_top", None)
        self.candidate_to_top = nn.ParameterList()
        self.register_parameter("current_candidate_to_top", None)
        # Create the dendrite layer
        self.dendrite_module = PAIDendriteModule(
            self.main_module,
            activation_function_value=self.activation_function_value,
            name=self.name,
            input_dimensions=self.this_input_dimensions,
        )
        # If it is linear and default has convolutional dimensions, automatically set to just be batch size and neuron indexes
        if (
            issubclass(type(start_module), nn.Linear)
            or (
                issubclass(type(start_module), GPA.PAISequential)
                and issubclass(type(start_module.model[0]), nn.Linear)
            )
        ) and (
            np.array(self.this_input_dimensions)[2:] == -1
        ).all():  # Everything past 2 is a negative 1
            self.set_this_input_dimensions(self.this_input_dimensions[0:2])
        GPA.pai_tracker.add_pai_neuron_module(self)

    def __getattr__(self, name):
        """Get member variables from the main module.

        Parameters
        ----------
        name : str
            The name of the variable to retrieve.
        Returns
        -------
        The requested variable.

        Notes
        -----
        This method first attempts to retrieve the attribute from the PAINeuronModule instance.
        If it fails, it tries to get the attribute from the wrapped main_module.
        This allows seamless access to the main module's attributes without modifying original code.
        """
        try:
            return super().__getattr__(name)
        except AttributeError:
            return getattr(self.main_module, name)

    def clear_processors(self):
        """Clear processors if they save values for DeepCopy and save.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        if not self.processor:
            return
        else:
            self.processor.clear_processor()
            self.dendrite_module.clear_processors()

    def clear_dendrites(self):
        """Clear and reset dendrites before loading from a state dict.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        self.dendrite_modules_added = 0
        self.dendrites_to_top = nn.ParameterList()
        self.candidate_to_top = nn.ParameterList()
        self.dendrite_module = PAIDendriteModule(
            self.main_module,
            activation_function_value=self.activation_function_value,
            name=self.name,
            input_dimensions=self.this_input_dimensions,
        )

    def __str__(self):
        """String representation of the layer.

        Parameters
        ----------
        None

        Returns
        -------
        str
            String representation of the layer.

        Notes
        -----
        Setting for verbose changes level of details in the string output.
        """
        # If verbose print the whole module otherwise just print the module type as a PAIModule
        if GPA.pc.get_verbose():
            total_string = self.main_module.__str__()
            total_string = "PAIModule(" + total_string + ")"
            return total_string + self.dendrite_module.__str__()
        else:
            total_string = self.main_module.__str__()
            total_string = "PAIModule(" + total_string + ")"
            return total_string

    def __repr__(self):
        """Representation of the layer."""
        return self.__str__()

    def set_this_input_dimensions(self, new_input_dimensions):
        """Set the input dimensions for the neuron and dendrite blocks.

        Signals to this NeuronModule that its input dimensions are different
        than the global default.

        Parameters
        ----------
        new_input_dimensions : list
            A list or tensor specifying the new input dimensions.
        Returns
        -------
        None

        """
        if type(new_input_dimensions) is list:
            new_input_dimensions = torch.tensor(new_input_dimensions)
        delattr(self, "this_input_dimensions")
        self.register_buffer(
            "this_input_dimensions", new_input_dimensions.detach().clone()
        )
        if (new_input_dimensions == 0).sum() != 1:
            print(f"6 need exactly one 0 in the input dimensions: {self.name}")
            print(new_input_dimensions)
        self.this_node_index.copy_(
            (new_input_dimensions == 0).nonzero(as_tuple=True)[0][0]
        )
        self.dendrite_module.set_this_input_dimensions(new_input_dimensions)

    def set_mode(self, mode):
        """Switch between neuron training and dendrite training.

        Parameters
        ----------
        mode : str
            The mode to set. Either "n" for neuron training or "p" for pai-dendrite training.

        Returns
        -------
        bool
            True if mode was set successfully, False otherwise.

        Notes
        -----
        If False is returned, the mode was not changed due to an error.
        This is a problem that should not be ignored, but it can be ignored
        by calling PGA.pc.set_checked_skipped_modules(True)
        """

        if GPA.pc.get_verbose():
            print(f"{self.name} calling set mode {mode}")
        # If returning to neuron training
        if mode == "n":
            self.dendrite_module.set_mode(mode)
            # Initialize the dendrite to neuron connections
            if self.dendrite_modules_added > 0:
                if GPA.pc.get_learn_dendrites_live():
                    values = torch.cat(
                        (
                            self.dendrites_to_top[self.dendrite_modules_added - 1],
                            nn.Parameter(self.candidate_to_top.detach().clone()),
                        ),
                        0,
                    )
                else:
                    values = torch.cat(
                        (
                            self.dendrites_to_top[self.dendrite_modules_added - 1],
                            nn.Parameter(
                                torch.zeros(
                                    (1, self.out_channels),
                                    device=self.dendrites_to_top[
                                        self.dendrite_modules_added - 1
                                    ].device,
                                    dtype=GPA.pc.get_d_type(),
                                )
                            ),
                        ),
                        0,
                    )
                self.dendrites_to_top.append(
                    nn.Parameter(
                        values.detach().clone().to(GPA.pc.get_device()),
                        requires_grad=True,
                    )
                )
            else:
                if GPA.pc.get_learn_dendrites_live():
                    self.dendrites_to_top.append(
                        nn.Parameter(
                            self.candidate_to_top.detach().clone(), requires_grad=True
                        )
                    )
                else:
                    self.dendrites_to_top.append(
                        nn.Parameter(
                            torch.zeros(
                                (1, self.out_channels),
                                device=GPA.pc.get_device(),
                                dtype=GPA.pc.get_d_type(),
                            )
                            .detach()
                            .clone(),
                            requires_grad=True,
                        )
                    )
            self.dendrite_modules_added += 1
            if GPA.pc.get_perforated_backpropagation():
                MPB.set_module_n_pb(self)
        # If starting dendrite training
        else:
            try:
                # Save the values that were calculated in filter_backward
                self.out_channels = self.dendrite_module.dendrite_values[0].out_channels
                self.dendrite_module.out_channels = (
                    self.dendrite_module.dendrite_values[0].out_channels
                )
            except Exception as e:
                print(e)
                print(
                    f"this occurred in layer: {self.dendrite_module.dendrite_values[0].layer_name}"
                )
                print(
                    "Module should be added to module_names_to_track so it doesn't have dendrites added"
                )
                print("If you are getting here but out_channels has not been set")
                print(
                    "A common reason is that this layer never had gradients flow through it."
                )
                print("I have seen this happen because:")
                print("-The weights were frozen (requires_grad = False)")
                print(
                    "-A model is added but not used so it was converted but never PAI initialized"
                )
                print(
                    "-A module was converted that doesn't have weights that get modified so backward doesn't flow through it"
                )
                print(
                    "If this is normal behavior set GPA.pc.set_checked_skipped_modules(True) in the main to ignore"
                )
                print(
                    "You can also set right now in this pdb terminal to have this not happen more after checking all layers this cycle."
                )
                if not GPA.pc.get_checked_skipped_modules():
                    import pdb

                    pdb.set_trace()
                return False
            # Only change mode if it makes it past the above exception
            self.dendrite_module.set_mode(mode)
            if GPA.pc.get_perforated_backpropagation():
                MPB.set_module_p_pb(self)
        return True

    def create_new_dendrite_module(self):
        """Add an additional dendrite module.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.dendrite_module.create_new_dendrite_module()

    def forward(self, *args, **kwargs):
        """Forward pass through the neuron layer.

        Parameters
        ----------
        *args : tuple
            Positional arguments for the forward pass.
        **kwargs : dict
            Keyword arguments for the forward pass.

        Returns
        -------
        Any
            The output of the module after processing through the neuron and dendrite modules.

        Notes
        -----
            The output of this forward function will have the same format as the output
            of the original module
        """

        # If debugging all input dimensions, quit program on first forward call
        if GPA.pc.get_debugging_input_dimensions() == 2:
            print("all input dim problems now printed")
            sys.exit(0)
        if GPA.pc.get_extra_verbose():
            print(f"{self.name} calling forward")
        # Call the main modules forward
        out = self.main_module(*args, **kwargs)
        # Filter with the processor if required
        if self.processor is not None:
            out = self.processor.post_n1(out)
        # Call the forwards for all of the Dendrites
        (
            dendrite_outs,
            candidate_outs,
            candidate_nonlinear_outs,
            candidate_outs_non_zeroed,
        ) = self.dendrite_module(*args, **kwargs)
        # If there are dendrites add all of their outputs to the neurons output
        if self.dendrite_modules_added > 0:
            for i in range(0, self.dendrite_modules_added):
                to_top = self.dendrites_to_top[self.dendrite_modules_added - 1][i, :]
                for dim in range(len(dendrite_outs[i].shape)):
                    if dim == self.this_node_index:
                        continue
                    to_top = to_top.unsqueeze(dim)
                if GPA.pc.get_confirm_correct_sizes():
                    to_top = to_top.expand(
                        list(dendrite_outs[i].size())[0 : self.this_node_index]
                        + [self.out_channels]
                        + list(dendrite_outs[i].size())[self.this_node_index + 1 :]
                    )
                out = out + (dendrite_outs[i].to(out.device) * to_top.to(out.device))

        if GPA.pc.get_perforated_backpropagation():
            out = MPB.apply_pb(
                self,
                out,
                candidate_outs,
                candidate_nonlinear_outs,
                candidate_outs_non_zeroed,
            )
        # Catch if processors are required
        if type(out) is tuple:
            print(self)
            print(
                f"The output of the above module {self.name} is a tuple when it must be a single tensor"
            )
            print(
                "Look in the API customization.md at section 2.2 regarding processors to fix this."
            )
            import pdb

            pdb.set_trace()

        # Call filter backward to ensure the neuron index is setup correctly
        if out.requires_grad:
            if GPA.pc.get_perforated_backpropagation():
                MPB.setup_hooks(self, out, candidate_nonlinear_outs)
            else:
                out.register_hook(
                    lambda grad: filter_backward(
                        grad, self.dendrite_module.dendrite_values, {}
                    )
                )

        # If there is a processor apply the second neuron stage
        if self.processor is not None:
            out = self.processor.post_n2(out)

        return out


class TrackedNeuronModule(nn.Module):
    """Wrapper for modules you don't want to add dendrites to. Ensures all modules are accounted for."""

    def __init__(self, start_module, name):
        """Initialize TrackedNeuronModule.

        This function sets up the tracked neuron module to wrap the start_module
        without adding dendrites.

        Parameters
        ----------
        start_module : nn.Module
            The module to wrap.
        name : str
            The name of the neuron module.
        """
        super(TrackedNeuronModule, self).__init__()

        self.main_module = start_module
        self.name = name

        self.type = "tracked_module"
        set_tracked_params(self.main_module)
        if GPA.pc.get_verbose():
            print(
                f"tracking a layer {self.name} with main type {type(self.main_module)}"
            )
            print(start_module)
        GPA.pai_tracker.add_tracked_neuron_module(self)

    def __getattr__(self, name):
        """Get member variables from the main module.

        Parameters
        ----------
        name : str
            The name of the variable to retrieve.
        Returns
        -------
        The requested variable.

        Notes
        -----
        This method first attempts to retrieve the attribute from the PAINeuronModule instance.
        If it fails, it tries to get the attribute from the wrapped main_module.
        This allows seamless access to the main module's attributes without modifying original code.
        """
        try:
            return super().__getattr__(name)
        except AttributeError:
            return getattr(self.main_module, name)

    def set_mode(self, mode):
        """Set mode for tracked layer.

        Parameters
        ----------
        mode : str
            The mode to set. Either "n" for neuron training or "p" for pai-dendrite training.

        Returns
        -------
        bool
            True.

        Notes
        -----
        This function does not change any behavior since this is a tracked layer.
        """

        if GPA.pc.get_verbose():
            print(f"{self.name} calling set mode {mode}")
        return True

    def forward(self, *args, **kwargs):
        """Forward pass for tracked layer.

        Parameters
        ----------
        *args : tuple
            Positional arguments for the forward pass.
        **kwargs : dict
            Keyword arguments for the forward pass.

        Returns
        -------
        Any
            The output of the module

        Notes
        -----
            The output of this forward function will have the same format as the output
            of the original module
        """
        return self.main_module(*args, **kwargs)

    def __str__(self):
        """String representation of the layer.

        Parameters
        ----------
        None

        Returns
        -------
        str
            String representation of the layer.

        Notes
        -----
        Setting for verbose changes level of details in the string output.
        """

        if GPA.pc.get_verbose():
            total_string = self.main_module.__str__()
            total_string = "PAITrackedLayer(" + total_string + ")"
            return total_string
        else:
            total_string = self.main_module.__str__()
            total_string = "PAITrackedLayer(" + total_string + ")"
            return total_string

    def __repr__(self):
        """Representation of the layer."""
        return self.__str__()


def init_params(model):
    """Randomize weights after duplicating the main module for the next set of dendrites."""
    for param in model.parameters():
        param.data = (
            torch.randn(param.size(), dtype=param.dtype)
            * GPA.pc.get_candidate_weight_initialization_multiplier()
        )


class PAIDendriteModule(nn.Module):
    """Module containing all dendrites modules added to the neuron module."""

    def __init__(
        self,
        initial_module,
        activation_function_value=0.3,
        name="no_name_given",
        input_dimensions=None,
    ):
        """Initialize PAINeuronModule.

        This function sets up the dendrite module to create candidate and permanent
        dendrite modules based on the initial_module provided.

        Parameters
        ----------
        initial_module : nn.Module
            The module to copy.
        activation_function_value : float, optional
            A value associated with the activation function, by default 0.3.
        name : str
            The name of the neuron module.
        input_dimensions : vector, optional
            The dimensions of the input vector
        """
        super(PAIDendriteModule, self).__init__()

        if input_dimensions is None:
            input_dimensions = []

        self.layers = nn.ModuleList([])
        self.processors = []
        self.candidate_processors = []
        self.num_dendrites = 0
        # Number of dendrite cycles performed
        self.register_buffer(
            "num_cycles",
            torch.zeros(1, device=GPA.pc.get_device(), dtype=GPA.pc.get_d_type()),
        )
        self.mode = "n"
        self.name = name
        # Create a copy of the parent module so you don't have a pointer to the real one which causes save errors
        self.parent_module = UPA.deep_copy_pai(initial_module)
        # Setup the input dimensions and node index for combining dendrite outputs
        if GPA.pc.get_perforated_backpropagation():
            MPB.create_extra_tensors(self)
        if input_dimensions == []:
            self.register_buffer(
                "this_input_dimensions", torch.tensor(GPA.pc.get_input_dimensions())
            )
        else:
            self.register_buffer(
                "this_input_dimensions", input_dimensions.detach().clone()
            )
        if (self.this_input_dimensions == 0).sum() != 1:
            print(f"1 need exactly one 0 in the input dimensions: {self.name}")
            print(self.this_input_dimensions)
            sys.exit(-1)
        self.register_buffer(
            "this_node_index", torch.tensor(GPA.pc.get_input_dimensions().index(0))
        )

        # Initialize dendrite to dendrite connections
        self.dendrites_to_candidates = nn.ParameterList()
        self.dendrites_to_dendrites = nn.ParameterList()

        # Store an activation function value if required
        self.activation_function_value = activation_function_value
        self.dendrite_values = nn.ModuleList([])
        for j in range(0, GPA.pc.get_global_candidates()):
            if GPA.pc.get_verbose():
                print(f"creating dendrite Values for {self.name}")
            self.dendrite_values.append(
                DendriteValueTracker(
                    False,
                    self.activation_function_value,
                    self.name,
                    self.this_input_dimensions,
                )
            )

    def set_this_input_dimensions(self, new_input_dimensions):
        """Set input dimensions for dendrite layer.

        Signals to this DendriteModule that its input dimensions are different
        than the global default.

        Parameters
        ----------
        new_input_dimensions : list
            A list or tensor specifying the new input dimensions.
        Returns
        -------
        None

        """

        if type(new_input_dimensions) is list:
            new_input_dimensions = torch.tensor(new_input_dimensions)
        delattr(self, "this_input_dimensions")
        self.register_buffer(
            "this_input_dimensions", new_input_dimensions.detach().clone()
        )
        if (new_input_dimensions == 0).sum() != 1:
            print(f"2 Need exactly one 0 in the input dimensions: {self.name}")
            print(new_input_dimensions)
            sys.exit(-1)
        self.this_node_index.copy_(
            (new_input_dimensions == 0).nonzero(as_tuple=True)[0][0]
        )
        for j in range(0, GPA.pc.get_global_candidates()):
            self.dendrite_values[j].set_this_input_dimensions(new_input_dimensions)

    def create_new_dendrite_module(self):
        """Add a new set of dendrites."""
        # Candidate layer
        self.candidate_module = nn.ModuleList([])
        # Copy that is unused for open source version
        self.best_candidate_module = nn.ModuleList([])
        if GPA.pc.get_verbose():
            print(self.name)
            print("Setting candidate processors")
        self.candidate_processors = []
        with torch.no_grad():
            for i in range(0, GPA.pc.get_global_candidates()):

                new_module = UPA.deep_copy_pai(self.parent_module)
                init_params(new_module)
                if GPA.pc.get_perforated_backpropagation():
                    MPB.set_grad_params(new_module, True)
                self.candidate_module.append(new_module)
                self.best_candidate_module.append(UPA.deep_copy_pai(new_module))
                if type(self.parent_module) in GPA.pc.get_modules_with_processing():
                    module_index = GPA.pc.get_modules_with_processing().index(
                        type(self.parent_module)
                    )
                    self.candidate_processors.append(
                        GPA.pc.get_modules_processing_classes()[module_index]()
                    )
                elif (
                    type(self.parent_module).__name__
                    in GPA.pc.get_module_names_with_processing()
                ):
                    module_index = GPA.pc.get_module_names_with_processing().index(
                        type(self.parent_module).__name__
                    )
                    self.candidate_processors.append(
                        GPA.pc.get_module_by_name_processing_classes()[module_index]()
                    )

        for i in range(0, GPA.pc.get_global_candidates()):
            self.candidate_module[i].to(GPA.pc.get_device())
            self.best_candidate_module[i].to(GPA.pc.get_device())

        # Reset the dendrite_values objects
        for j in range(0, GPA.pc.get_global_candidates()):
            self.dendrite_values[j].reinitialize_for_pai()

        # If there are already dendrites initialize the dendrite to dendrite connections
        if self.num_dendrites > 0:
            self.dendrites_to_candidates = nn.ParameterList()
            for j in range(0, GPA.pc.get_global_candidates()):
                self.dendrites_to_candidates.append(
                    nn.Parameter(
                        torch.zeros(
                            (self.num_dendrites, self.out_channels),
                            device=GPA.pc.get_device(),
                            dtype=GPA.pc.get_d_type(),
                        ),
                        requires_grad=True,
                    )
                )
                if GPA.pc.get_perforated_backpropagation():
                    MPB.init_candidates(self, j)

    def clear_processors(self):
        """Clear processors."""
        for processor in self.processors:
            if not processor:
                continue
            else:
                processor.clear_processor()
        for processor in self.candidate_processors:
            if not processor:
                continue
            else:
                processor.clear_processor()

    def set_mode(self, mode):
        """Perform actions when switching between neuron and dendrite training.

        Parameters
        ----------
        mode : str
            The mode to set. Either "n" for neuron training or "p" for pai-dendrite training.

        Returns
        -------
        None
        """

        self.mode = mode
        self.num_cycles += 1
        if GPA.pc.get_verbose():
            print(f"PAI calling set mode {mode} : {self.num_cycles}")

        # When switching back to neuron training mode convert candidates layers into accepted layers
        if mode == "n":
            if GPA.pc.get_verbose():
                print("So calling all the things to add to layers")
            # Copy weights/bias from correct candidates
            if self.num_dendrites == 1:
                self.dendrites_to_dendrites = nn.ParameterList()
                self.dendrites_to_dendrites.append(torch.tensor([]))
            if self.num_dendrites >= 1:
                self.dendrites_to_dendrites.append(
                    torch.nn.Parameter(
                        torch.zeros(
                            [self.num_dendrites, self.out_channels],
                            device=GPA.pc.get_device(),
                            dtype=GPA.pc.get_d_type(),
                        ),
                        # Grad is true if not pb or if pb and dendrite_update_mode is true
                        requires_grad=(not GPA.pc.get_perforated_backpropagation())
                        or GPA.pc.get_dendrite_update_mode(),
                    )
                )
            with torch.no_grad():
                if GPA.pc.get_global_candidates() > 1:
                    print(
                        "This was a flag that will be needed if using multiple candidates. "
                        "It's not set up yet but nice work finding it."
                    )
                    pdb.set_trace()
                plane_max_index = 0
                self.layers.append(
                    UPA.deep_copy_pai(self.best_candidate_module[plane_max_index])
                )
                self.layers[self.num_dendrites].to(GPA.pc.get_device())
                if self.num_dendrites > 0:
                    self.dendrites_to_dendrites[self.num_dendrites].copy_(
                        self.dendrites_to_candidates[plane_max_index]
                    )
                if type(self.parent_module) in GPA.pc.get_modules_with_processing():
                    self.processors.append(self.candidate_processors[plane_max_index])
                if (
                    type(self.parent_module).__name__
                    in GPA.pc.get_module_names_with_processing()
                ):
                    self.processors.append(self.candidate_processors[plane_max_index])
            if GPA.pc.get_perforated_backpropagation():
                MPB.set_pb_mode(self, mode)
            del self.candidate_module, self.best_candidate_module

            self.num_dendrites += 1

    def forward(self, *args, **kwargs):
        """Forward pass for dendrite layer.

        Parameters
        ----------
        *args : tuple
            Positional arguments for the forward pass.
        **kwargs : dict
            Keyword arguments for the forward pass.

        Returns
        -------
        Any
            The output of the module after processing through the neuron and dendrite modules.
        Any
            Remaining outputs are only used for Perforated Backpropagation.
        Any
            Remaining outputs are only used for Perforated Backpropagation.
        Any
            Remaining outputs are only used for Perforated Backpropagation.

        Notes
        -----
        If using Perforated Backpropagation, the additional outputs will be moved around in
        this code but left unused and only passed into separate PB functions.
        """

        outs = {}

        # For all layers apply processors, call the layers, then apply post processors
        args2, kwargs2 = args, kwargs
        for c in range(0, self.num_dendrites):
            if GPA.pc.get_perforated_backpropagation():
                args2, kwargs2 = MPB.preprocess_pb(*args, **kwargs)
            if self.processors != []:
                args2, kwargs2 = self.processors[c].pre_d(*args2, **kwargs2)
            out_values = self.layers[c](*args2, **kwargs2)
            if self.processors != []:
                outs[c] = self.processors[c].post_d(out_values)
            else:
                outs[c] = out_values

        # Create dendrite outputs
        # Each dendrite has input from previously created dendrites
        # So activation is added before the nonlinearity is called
        view_tuple = []
        for out_index in range(0, self.num_dendrites):
            current_out = outs[out_index]
            view_tuple = []
            for dim in range(len(current_out.shape)):
                if dim == self.this_node_index:
                    view_tuple.append(-1)
                    continue
                view_tuple.append(1)

            for in_index in range(0, out_index):
                if view_tuple == [
                    1
                ]:  # This is only the case when passing a single datapoint rather than a batch
                    current_out = (
                        current_out
                        + self.dendrites_to_dendrites[out_index][in_index, :].to(
                            current_out.device
                        )
                        * outs[in_index]
                    )
                else:
                    current_out = (
                        current_out
                        + self.dendrites_to_dendrites[out_index][in_index, :]
                        .view(view_tuple)
                        .to(current_out.device)
                        * outs[in_index]
                    )
            outs[out_index] = GPA.pc.get_pai_forward_function()(current_out)
        # Return a dict which has all dendritic outputs after the activation functions were called
        if GPA.pc.get_perforated_backpropagation():
            candidate_outs, candidate_nonlinear_outs, candidate_non_zeroed = (
                MPB.forward_candidates(self, view_tuple, outs, *args2, **kwargs2)
            )
        else:
            candidate_outs, candidate_nonlinear_outs, candidate_non_zeroed = (
                {},
                {},
                {},
            )
        return outs, candidate_outs, candidate_nonlinear_outs, candidate_non_zeroed


class DendriteValueTracker(nn.Module):
    """Tracker object that maintains certain values for each set of dendrites."""

    def __init__(
        self,
        initialized,
        activation_function_value,
        name,
        input_dimensions,
        out_channels=-1,
    ):
        """Initialize DendriteValueTracker.

        This function sets up the value tracker to maintain statistics and values
        for each set of dendrites.

        Parameters
        ----------
        initialized : int
            Whether the dendrite has been initialized (1) or not (0).
        activation_function_value : float
            A value associated with the activation function.
        name : str
            The name of the associated neuron module.
        input_dimensions : vector
            The dimensions of the input vector.
        out_channels : int
            The number of output channels
        """
        super(DendriteValueTracker, self).__init__()

        self.layer_name = name
        for val_name in DENDRITE_INIT_VALUES:
            self.register_buffer(
                val_name,
                torch.zeros(1, device=GPA.pc.get_device(), dtype=GPA.pc.get_d_type()),
            )
        self.initialized[0] = initialized
        self.activation_function_value = activation_function_value
        self.register_buffer("this_input_dimensions", input_dimensions.clone().detach())
        if (self.this_input_dimensions == 0).sum() != 1:
            print(f"3 need exactly one 0 in the input dimensions: {self.layer_name}")
            print(self.this_input_dimensions)
            sys.exit(-1)
        self.register_buffer(
            "this_node_index", (input_dimensions == 0).nonzero(as_tuple=True)[0]
        )
        if out_channels != -1:
            self.setup_arrays(out_channels)
        else:
            self.out_channels = -1

    def print(self):
        """Print value tracker information."""
        total_string = "Value Tracker:"
        for val_name in DENDRITE_INIT_VALUES:
            total_string += f"\t{val_name}:\n\t\t"
            total_string += getattr(self, val_name).__repr__()
            total_string += "\n"
        for val_name in DENDRITE_TENSOR_VALUES:
            if getattr(self, val_name, None) is not None:
                total_string += f"\t{val_name}:\n\t\t"
                total_string += getattr(self, val_name).__repr__()
                total_string += "\n"
        print(total_string)

    def set_this_input_dimensions(self, new_input_dimensions):
        """Set input dimensions for value tracker

        Signals to this DendriteValueTracker that its input dimensions are different
        than the global default.

        Parameters
        ----------
        new_input_dimensions : list
            A list or tensor specifying the new input dimensions.
        Returns
        -------
        None

        """
        if type(new_input_dimensions) is list:
            new_input_dimensions = torch.tensor(new_input_dimensions)
        delattr(self, "this_input_dimensions")
        self.register_buffer(
            "this_input_dimensions", new_input_dimensions.detach().clone()
        )
        if (new_input_dimensions == 0).sum() != 1:
            print(f"4 need exactly one 0 in the input dimensions: {self.layer_name}")
            print(new_input_dimensions)
            sys.exit(-1)
        self.this_node_index.copy_(
            (new_input_dimensions == 0).nonzero(as_tuple=True)[0][0]
        )

    def set_out_channels(self, shape_values):
        """Set output channels based on shape values and saved node index

        Parameters
        ----------
        shape_values : list or torch.Size
            A list or tensor specifying the shape values.

        Returns
        -------
        None
        """
        if type(shape_values) == torch.Size:
            self.out_channels = int(shape_values[self.this_node_index])
        else:
            self.out_channels = int(shape_values[self.this_node_index].item())

    def setup_arrays(self, out_channels):
        """Setup arrays for value tracker.

        Parameters
        ----------
        out_channels : int
            The number of output channels.
        Returns
        -------
        None

        """
        self.out_channels = out_channels
        for val_name in DENDRITE_TENSOR_VALUES:
            self.register_buffer(
                val_name,
                torch.zeros(
                    out_channels, device=GPA.pc.get_device(), dtype=GPA.pc.get_d_type()
                ),
            )

        for name in VALUE_TRACKER_ARRAYS:
            setattr(self, name, {})
            count = 1
            if torch.cuda.device_count() > count:
                count = torch.cuda.device_count()
            for i in range(count):
                getattr(self, name)[i] = []
        for val_name in DENDRITE_SINGLE_VALUES:
            self.register_buffer(
                val_name,
                torch.zeros(1, device=GPA.pc.get_device(), dtype=GPA.pc.get_d_type()),
            )

    def reinitialize_for_pai(self):
        """Reinitialize value tracker to add the next set of dendrites"""

        if self.out_channels == -1:
            print("You have a converted module that was never initialized")
            print("This likely means it not being added to the autograd graph")
            print("Check your forward function that it is actually being used")
            print("If its not you should really delete it, but you can also add")
            print(
                "the name below to GPA.pc.get_module_ids_to_track() to not convert it"
            )
            print(self.layer_name)
            print("with:")
            print("GPA.pc.get_module_names_to_track() += ['" + self.layer_name + "']")
            print("This can also happen while testing_dendrite_capacity if you")
            print(
                "run a validation cycle and try to add Dendrites before doing any training.\n"
            )

        self.initialized[0] = 0
        if GPA.pc.get_perforated_backpropagation():
            MPB.reinitialize_for_pb(self)
        else:
            for val_name in DENDRITE_REINIT_VALUES:
                setattr(self, val_name, getattr(self, val_name) * 0)
