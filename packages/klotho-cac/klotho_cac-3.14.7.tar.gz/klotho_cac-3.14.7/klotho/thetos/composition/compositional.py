from typing import Union, Optional, Any
from fractions import Fraction
import pandas as pd

from klotho.chronos import TemporalUnit, RhythmTree, Meas
from klotho.chronos.temporal_units.temporal import Chronon
from klotho.thetos.parameters import ParameterTree
from klotho.thetos.instruments import Instrument
from klotho.dynatos.envelopes import Envelope


class Event(Chronon):
    """
    An enhanced Chronon that includes parameter field access.
    
    Extends the basic temporal event data (start, duration, etc.) with 
    access to musical parameters stored in a synchronized ParameterTree.
    """
    
    __slots__ = ('_pt',)
    
    def __init__(self, node_id: int, rt: RhythmTree, pt: ParameterTree):
        super().__init__(node_id, rt)
        self._pt = pt
    
    @property
    def parameters(self):
        """
        Get all active parameter fields for this event.
        
        Returns
        -------
        dict
            Dictionary of active parameter field names and values
        """
        return self._pt[self._node_id].active_items()
    
    def get_parameter(self, key: str, default=None):
        """
        Get a specific parameter value for this event.
        
        Parameters
        ----------
        key : str
            The parameter field name to retrieve
        default : Any, optional
            Default value if parameter not found
            
        Returns
        -------
        Any
            The parameter value or default
        """
        value = self._pt.get(self._node_id, key)
        return value if value is not None else default
    
    def __getitem__(self, key: str):
        """
        Access temporal or parameter attributes by key.
        
        Parameters
        ----------
        key : str
            Attribute name (temporal property or parameter field)
            
        Returns
        -------
        Any
            The requested attribute value
        """
        temporal_attrs = {'start', 'duration', 'end', 'proportion', 'metric_duration', 'node_id', 'is_rest'}
        if key in temporal_attrs:
            return getattr(self, key)
        return self.get_parameter(key)


class CompositionalUnit(TemporalUnit):
    """
    A TemporalUnit enhanced with synchronized parameter management capabilities.
    
    Extends TemporalUnit to include a shadow ParameterTree that maintains 
    identical structural form to the internal RhythmTree. This allows for 
    hierarchical parameter organization where parameter values can be set at 
    any level and automatically propagate to descendant events.
    
    Parameters
    ----------
    span : Union[int, float, Fraction], default=1
        Number of measures the unit spans
    tempus : Union[Meas, Fraction, int, float, str], default='4/4'
        Time signature (e.g., '4/4', Meas(4,4))
    prolatio : Union[tuple, str], default='d'
        Subdivision pattern (tuple) or type ('d', 'r', 'p', 's')
    beat : Union[None, Fraction, int, float, str], optional
        Beat unit for tempo (e.g., Fraction(1,4) for quarter note)
    bpm : Union[None, int, float], optional
        Beats per minute
    offset : float, default=0
        Start time offset in seconds
    pfields : Union[dict, list, None], optional
        Parameter fields to initialize. Can be:
        - dict: {field_name: default_value, ...}
        - list: [field_name1, field_name2, ...] (defaults to 0.0)
        - None: No parameter fields initially
        
    Attributes
    ----------
    pt : ParameterTree
        The synchronized parameter tree matching RhythmTree structure (returns copy)
    pfields : list
        List of all available parameter field names
    """
    
    def __init__(self,
                 span     : Union[int, float, Fraction]            = 1,
                 tempus   : Union[Meas, Fraction, int, float, str] = '4/4',
                 prolatio : Union[tuple, str]                      = 'd',
                 beat     : Union[None, Fraction, int, float, str] = None,
                 bpm      : Union[None, int, float]                = None,
                 offset   : float                                  = 0,
                 inst     : Union[Instrument, None]                = None,
                 mfields  : Union[dict, list, None]                = None,
                 pfields  : Union[dict, list, None]                = None):
        
        super().__init__(span, tempus, prolatio, beat, bpm, offset)
        
        if mfields is None:
            mfields = {}
        if 'group' not in mfields:
            mfields['group'] = 'default'
        
        self._pt = self._create_synchronized_parameter_tree(pfields, inst, mfields)
        
        self._envelopes = {}
        self._next_envelope_id = 0
        self._envelope_offset = offset
    
    @classmethod
    def from_rt(cls, rt: RhythmTree, beat: Union[None, Fraction, int, float, str] = None, bpm: Union[None, int, float] = None, pfields: Union[dict, list, None] = None, mfields: Union[dict, list, None] = None, inst: Union[Instrument, None] = None):
        return cls(span     = rt.span,
                   tempus   = rt.meas,
                   prolatio = rt.subdivisions,
                   beat     = beat,
                   bpm      = bpm,
                   offset   = 0,
                   pfields  = pfields,
                   mfields  = mfields,
                   inst     = inst)
        
    @classmethod
    def from_ut(cls, ut: TemporalUnit, pfields: Union[dict, list, None] = None, mfields: Union[dict, list, None] = None, inst: Union[Instrument, None] = None):
        return cls(span     = ut.span,
                   tempus   = ut.tempus,
                   prolatio = ut.prolationis,
                   beat     = ut.beat,
                   bpm      = ut.bpm,
                   offset   = ut.offset,
                   pfields  = pfields,
                   mfields  = mfields,
                   inst     = inst)
    
    def _create_synchronized_parameter_tree(self, pfields: Union[dict, list, None], inst: Union[Instrument, None] = None, mfields: Union[dict, list, None] = None) -> ParameterTree:
        """
        Create a ParameterTree with identical structure to the RhythmTree but blank node data.
        
        Parameters
        ----------
        pfields : Union[dict, list, None]
            Parameter fields to initialize
        inst : Union[Instrument, None], optional
            Instrument to set on the root node
        mfields : Union[dict, list, None], optional
            Meta fields to initialize
            
        Returns
        -------
        ParameterTree
            A parameter tree matching the rhythm tree structure with clean nodes
        """
        pt = ParameterTree(self._rt.meas.numerator, self._rt.subdivisions)
        
        for node in pt.nodes:
            node_data = pt[node]
            node_data.clear()
        
        if pfields is not None:
            self._initialize_parameter_fields(pt, pfields)
        
        if inst is not None:
            pt.set_instrument(pt.root, inst)
        
        if mfields is not None:
            self._initialize_meta_fields(pt, mfields)
        
        return pt
    
    def _initialize_parameter_fields(self, pt: ParameterTree, pfields: Union[dict, list]):
        """
        Initialize parameter fields across all nodes in the parameter tree.
        
        Parameters
        ----------
        pt : ParameterTree
            The parameter tree to initialize
        pfields : Union[dict, list]
            Parameter fields to set
        """
        if isinstance(pfields, dict):
            pt.set_pfields(pt.root, **pfields)
        elif isinstance(pfields, list):
            default_values = {field: 0.0 for field in pfields}
            pt.set_pfields(pt.root, **default_values)

    def _initialize_meta_fields(self, pt: ParameterTree, mfields: Union[dict, list]):
        """
        Initialize meta fields across all nodes in the parameter tree.
        
        Parameters
        ----------
        pt : ParameterTree
            The parameter tree to initialize
        mfields : Union[dict, list]
            Meta fields to set
        """
        if isinstance(mfields, dict):
            pt.set_mfields(pt.root, **mfields)
        elif isinstance(mfields, list):
            default_values = {field: '' for field in mfields}
            pt.set_mfields(pt.root, **default_values)

    def _validate_non_overlapping_subtrees(self, nodes):
        """Ensure no node is a descendant of another in the list"""
        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if i != j and node2 in self._pt.descendants(node1):
                    raise ValueError(f"Node {node2} is a descendant of node {node1}. Overlapping subtrees not allowed for envelope assignment.")

    def _evaluate_envelopes(self):
        """Evaluate all envelopes and update parameter tree with computed values"""
        if not self._envelopes:
            return
        
        # Ensure temporal evaluation has occurred before accessing real_onset
        if self._events is None:
            self._events = super()._evaluate()
            
        offset_diff = self._offset - self._envelope_offset
        
        for envelope_id, env_data in self._envelopes.items():
            envelope = env_data['envelope']
            # Adjust start_time for offset changes
            start_time = env_data['start_time'] + offset_diff
            
            for node in env_data['affected_nodes']:
                event_time = self._rt[node]['real_onset']
                relative_time = event_time - start_time
                
                relative_time = max(0, min(relative_time, envelope.total_time))
                
                try:
                    envelope_value = envelope.at_time(relative_time)
                except ValueError:
                    envelope_value = envelope._values[0] if relative_time <= 0 else envelope._values[-1]
                
                pfield_updates = {pfield: envelope_value for pfield in env_data['pfields']}
                if pfield_updates:
                    self._pt.set_pfields(node, **pfield_updates)
        
        # Update envelope offset to current offset for future calculations
        self._envelope_offset = self._offset

    def _evaluate(self):
        """
        Updates node timings and returns Event objects instead of Chronon objects.
        
        Returns
        -------
        tuple of Event
            Events containing both temporal and parameter data
        """
        super()._evaluate()
        self._evaluate_envelopes()
        leaf_nodes = self._rt.leaf_nodes
        return tuple(Event(node_id, self._rt, self._pt) for node_id in leaf_nodes)
    
    @property
    def pt(self) -> ParameterTree:
        """
        The ParameterTree of the CompositionalUnit (returns a copy).
        
        Returns
        -------
        ParameterTree
            A copy of the parameter tree maintaining structural synchronization with RhythmTree
        """
        return self._pt.copy()
    
    @property
    def pfields(self) -> list:
        """
        List of all available parameter field names.
        
        Returns
        -------
        list of str
            Sorted list of parameter field names
        """
        return self._pt.pfields
    
    @property
    def mfields(self) -> list:
        """
        List of all available meta field names.
        
        Returns
        -------
        list of str
            Sorted list of meta field names
        """
        return self._pt.mfields
    
    @property
    def events(self):
        """
        Enhanced events DataFrame including both temporal and parameter data.
        
        Returns
        -------
        pandas.DataFrame
            DataFrame with temporal properties and all parameter fields
        """
        if self._events is None:
            self._events = self._evaluate()
        base_data = []
        for event in self._events:
            event_dict = {
                'node_id': event.node_id,
                'start': event.start,
                'duration': event.duration,
                'end': event.end,
                'is_rest': event.is_rest,
                's': event.proportion,
                'metric_duration': event.metric_duration,
            }
            event_dict.update(event.parameters)
            base_data.append(event_dict)
        
        return pd.DataFrame(base_data, index=range(len(self._events)))
    
    def set_pfields(self, node: Union[int, list], endpoint: bool = True, **kwargs) -> None:
        """
        Set parameter field values for a specific node(s) and their descendants.
        
        Parameters
        ----------
        node : Union[int, list]
            The node ID(s) to set parameters for
        endpoint : bool, default=True
            Whether envelope spans through complete duration of final nodes (True)
            or only to their onset times (False)
        **kwargs
            Parameter field names and values to set (can include Envelope instances)
        """
        nodes = [node] if not isinstance(node, (list, tuple, set)) else list(node)
        
        envelope_fields = {k: v for k, v in kwargs.items() if isinstance(v, Envelope)}
        static_fields = {k: v for k, v in kwargs.items() if not isinstance(v, Envelope)}
        
        if envelope_fields and len(nodes) > 1:
            self._validate_non_overlapping_subtrees(nodes)
        
        for n in nodes:
            if static_fields:
                self._pt.set_pfields(n, **static_fields)
        for n in nodes:
            for pfield, envelope in envelope_fields.items():
                affected_nodes = set(self._pt.descendants(n))
                if n in self._pt.leaf_nodes:
                    affected_nodes.add(n)
                
                if self._events is None:
                    self._events = self._evaluate()
                
                start_time = min(self._rt[desc]['real_onset'] for desc in affected_nodes)
                
                if endpoint:
                    end_time = max(self._rt[desc]['real_onset'] + abs(self._rt[desc]['real_duration']) 
                                 for desc in affected_nodes)
                else:
                    end_time = max(self._rt[desc]['real_onset'] for desc in affected_nodes)
                
                envelope_duration = end_time - start_time
                scaled_envelope = Envelope(
                    values=envelope._original_values,
                    times=envelope._original_times,
                    curve=envelope._curve,
                    normalize_values=envelope._normalize_values,
                    normalize_times=envelope._normalize_times,
                    value_scale=envelope._value_scale,
                    time_scale=envelope_duration / envelope.total_time if envelope.total_time > 0 else 1.0,
                    resolution=envelope._resolution
                )
                
                envelope_id = self._next_envelope_id
                self._next_envelope_id += 1
                
                self._envelopes[envelope_id] = {
                    'envelope': scaled_envelope,
                    'affected_nodes': affected_nodes,
                    'pfields': [pfield],
                    'start_time': start_time,
                    'duration': envelope_duration
                }
        
        self._evaluate_envelopes()

    def set_mfields(self, node: Union[int, list], **kwargs) -> None:
        """
        Set meta field values for a specific node(s) and their descendants.
        
        Meta fields are static metadata that don't support envelope automation.
        
        Parameters
        ----------
        node : Union[int, list]
            The node ID(s) to set meta fields for
        **kwargs
            Meta field names and values to set
        """
        nodes = [node] if not isinstance(node, (list, tuple, set)) else list(node)
        
        for n in nodes:
            self._pt.set_mfields(n, **kwargs)

    def apply_envelope(self, level: Union[int, str], range_span: Union[tuple, int, None], envelope: Envelope, pfields: Union[str, list], endpoint: bool = True) -> int:
        """
        Apply envelope to a consecutive span of nodes at a specific level.
        
        Parameters
        ----------
        level : Union[int, str]
            Tree depth level, or "leaf" to select from leaf nodes directly
        range_span : Union[tuple, int, None]
            Node selection span. Can be:
            - None: all nodes at the level
            - int: from this index to end of level  
            - (start, end): inclusive range from start to end
        envelope : Envelope
            Envelope to apply
        pfields : Union[str, list]
            Parameter field name(s) to affect
        endpoint : bool, default=True
            Whether envelope spans through complete duration of final nodes (True)
            or only to their onset times (False)
            
        Returns
        -------
        int
            Envelope ID for reference
        """
        if level == "leaf":
            available_nodes = list(self._pt.leaf_nodes)
            affected_nodes = set()
        else:
            available_nodes = self._pt.at_depth(level)
            affected_nodes = set()
        
        if not available_nodes:
            level_desc = "leaf nodes" if level == "leaf" else f"level {level}"
            raise ValueError(f"No nodes found at {level_desc}")
        
        if range_span is None:
            start_pos, end_pos = 0, len(available_nodes) - 1
        elif isinstance(range_span, int):
            start_pos = range_span
            if start_pos < 0:
                start_pos = len(available_nodes) + start_pos
            end_pos = len(available_nodes) - 1
        else:
            start_pos, end_pos = range_span
            if start_pos < 0:
                start_pos = len(available_nodes) + start_pos
            if end_pos < 0:
                end_pos = len(available_nodes) + end_pos
            
        if start_pos < 0 or end_pos >= len(available_nodes) or start_pos > end_pos:
            level_desc = "leaf nodes" if level == "leaf" else f"level {level}"
            raise ValueError(f"Invalid range ({start_pos}, {end_pos}) for {level_desc} with {len(available_nodes)} nodes")
        
        span_nodes = available_nodes[start_pos:end_pos+1]
        
        if level == "leaf":
            affected_nodes = set(span_nodes)
        else:
            for node in span_nodes:
                affected_nodes.update(self._pt.descendants(node))
                if node in self._pt.leaf_nodes:
                    affected_nodes.add(node)
        
        if self._events is None:
            self._events = self._evaluate()
        
        start_time = min(self._rt[node]['real_onset'] for node in affected_nodes)
        
        if endpoint:
            end_time = max(self._rt[node]['real_onset'] + abs(self._rt[node]['real_duration']) 
                          for node in affected_nodes)
        else:
            end_time = max(self._rt[node]['real_onset'] for node in affected_nodes)
        
        envelope_duration = end_time - start_time
        
        scaled_envelope = Envelope(
            values=envelope._original_values,
            times=envelope._original_times,
            curve=envelope._curve,
            normalize_values=envelope._normalize_values,
            normalize_times=envelope._normalize_times,
            value_scale=envelope._value_scale,
            time_scale=envelope_duration / envelope.total_time if envelope.total_time > 0 else 1.0,
            resolution=envelope._resolution
        )
        
        envelope_id = self._next_envelope_id
        self._next_envelope_id += 1
        
        pfields_list = pfields if isinstance(pfields, list) else [pfields]
        
        self._envelopes[envelope_id] = {
            'envelope': scaled_envelope,
            'affected_nodes': affected_nodes,
            'pfields': pfields_list,
            'start_time': start_time,
            'duration': envelope_duration
        }
        
        self._evaluate_envelopes()
        
        return envelope_id
    
    def apply_slur(self, level: Union[int, str], range_span: Union[tuple, int, None]) -> int:
        """
        Apply slur to a consecutive span of nodes at a specific level.
        
        Parameters
        ----------
        level : Union[int, str]
            Tree depth level, or "leaf" to select from leaf nodes directly
        range_span : Union[tuple, int, None]
            Node selection span. Can be:
            - None: all nodes at the level
            - int: from this index to end of level  
            - (start, end): inclusive range from start to end
            
        Returns
        -------
        int
            Slur ID for reference
        """
        if level == "leaf":
            available_nodes = list(self._pt.leaf_nodes)
        else:
            available_nodes = self._pt.at_depth(level)
        
        if not available_nodes:
            level_desc = "leaf nodes" if level == "leaf" else f"level {level}"
            raise ValueError(f"No nodes found at {level_desc}")
        
        if range_span is None:
            start_pos, end_pos = 0, len(available_nodes) - 1
        elif isinstance(range_span, int):
            start_pos = range_span
            if start_pos < 0:
                start_pos = len(available_nodes) + start_pos
            end_pos = len(available_nodes) - 1
        else:
            start_pos, end_pos = range_span
            if start_pos < 0:
                start_pos = len(available_nodes) + start_pos
            if end_pos < 0:
                end_pos = len(available_nodes) + end_pos
        
        if start_pos < 0 or end_pos >= len(available_nodes) or start_pos > end_pos:
            level_desc = "leaf nodes" if level == "leaf" else f"level {level}"
            raise ValueError(f"Invalid range ({start_pos}, {end_pos}) for {level_desc} with {len(available_nodes)} nodes")
        
        span_nodes = available_nodes[start_pos:end_pos+1]
        
        if level == "leaf":
            affected_nodes = set(span_nodes)
        else:
            affected_nodes = set()
            for node in span_nodes:
                affected_nodes.update(self._pt.descendants(node))
                if node in self._pt.leaf_nodes:
                    affected_nodes.add(node)
        
        affected_nodes = {node for node in affected_nodes if node in self._pt.leaf_nodes}
        if self._events is None:
            self._events = self._evaluate()
        affected_nodes = {node for node in affected_nodes if not self._events[self._rt.leaf_nodes.index(node)].is_rest}
        
        if not affected_nodes:
            raise ValueError("No non-rest nodes found in slur span")
        
        return self._pt.add_slur(affected_nodes, self._rt, self._events)
    
    def set_instrument(self, node: int, instrument: Instrument, exclude: Union[str, list, set, None] = None) -> None:
        """
        Set an instrument for a specific node, applying its parameter fields.
        
        Parameters
        ----------
        node : int
            The node ID to set the instrument for
        instrument : Instrument
            The instrument to apply
        exclude : Union[str, list, set, None], optional
            Parameter fields to exclude from application
        """
        self._pt.set_instrument(node, instrument, exclude)
    
    def get_parameter(self, node: int, key: str, default=None):
        """
        Get a parameter value for a specific node.
        
        Parameters
        ----------
        node : int
            The node ID to query
        key : str
            The parameter field name
        default : Any, optional
            Default value if parameter not found
            
        Returns
        -------
        Any
            The parameter value or default
        """
        return self._pt.get(node, key) or default
    
    def clear_parameters(self, node: int = None) -> None:
        """
        Clear parameter values for a node and its descendants.
        
        Parameters
        ----------
        node : int, optional
            The node ID to clear. If None, clears all nodes
        """
        if node is None:
            self._envelopes.clear()
        else:
            to_remove = []
            for envelope_id, env_data in self._envelopes.items():
                if node in env_data['affected_nodes']:
                    to_remove.append(envelope_id)
            for envelope_id in to_remove:
                del self._envelopes[envelope_id]
        
        self._pt.clear(node)
    
    def get_event_parameters(self, idx: int) -> dict:
        """
        Get all parameter values for a specific event by index.
        
        Parameters
        ----------
        idx : int
            Event index
            
        Returns
        -------
        dict
            Dictionary of parameter field names and values
        """
        if self._events is None:
            self._events = self._evaluate()
        return self._events[idx].parameters
    
    def from_subtree(self, node: int) -> 'CompositionalUnit':
        """
        Create a new CompositionalUnit from a subtree of this one.
        
        This method extracts a subtree and preserves envelopes that are entirely
        contained within the subtree. Envelopes that cross subtree boundaries
        are discarded according to the design requirements.
        
        Parameters
        ----------
        node : int
            The root node of the subtree to extract
            
        Returns
        -------
        CompositionalUnit
            A new CompositionalUnit containing the subtree
        """
        # Extract the RhythmTree subtree (RhythmTree creates a new tree from subdivisions)
        rt_subtree = self._rt.subtree(node, renumber=True)
        
        # Create a new CompositionalUnit from the RhythmTree
        # This will create a synchronized ParameterTree with the same structure
        new_cu = self.__class__.from_rt(rt_subtree, beat=self.beat, bpm=self.bpm, pfields=self.pfields)
        
        # Preserve rest information from the original subtree
        # The from_rt method creates a new RhythmTree which loses rest info, so we need to restore it
        for orig_node, new_node in zip(rt_subtree.nodes, new_cu._rt.nodes):
            orig_proportion = rt_subtree[orig_node].get('proportion')
            if orig_proportion is not None and orig_proportion < 0:
                # This was a rest in the original subtree, make it a rest in the new tree
                new_cu.make_rest(new_node)
        
        # Copy parameter data from the original subtree nodes to the new structure
        # Since RhythmTree.subtree creates a new tree rather than extracting nodes,
        # we need to copy the parameter data appropriately
        original_subtree_nodes = [node] + list(self._rt.descendants(node))
        
        # First, copy any instrument assignments that apply to this subtree
        # When copying the full tree (node == root), preserve ALL instruments
        # When copying a subtree, only preserve the governing instrument
        if node == self._rt.root:
            # Full tree copy - preserve ALL instruments with proper node mapping
            old_to_new_mapping = {}
            old_nodes = [node] + list(self._rt.descendants(node))
            new_nodes = list(new_cu._pt.nodes)
            
            # Create mapping based on tree structure (breadth-first traversal order)
            for i, old_node in enumerate(old_nodes):
                if i < len(new_nodes):
                    old_to_new_mapping[old_node] = new_nodes[i]
            
            # Copy all instruments using the mapping
            for old_node, instrument in self._pt._node_instruments.items():
                if old_node in old_to_new_mapping:
                    new_node = old_to_new_mapping[old_node]
                    new_cu.set_instrument(new_node, instrument)
        else:
            # Subtree copy - only preserve governing instrument (original behavior)
            governing_instrument_node = self._pt.get_governing_subtree_node(node)
            if governing_instrument_node is not None and governing_instrument_node in self._pt._node_instruments:
                instrument = self._pt._node_instruments[governing_instrument_node]
                new_cu.set_instrument(new_cu._pt.root, instrument)
        
        # Copy parameter data from all nodes in the original subtree to corresponding nodes in the new tree
        # Since RhythmTree.subtree creates a completely new tree structure with renumbered nodes,
        # we need to map the parameter data appropriately
        new_tree_nodes = list(new_cu._pt.nodes)
        
        # Create a mapping based on tree structure position
        # Both trees should have the same relative structure
        for i, new_node in enumerate(new_tree_nodes):
            if i < len(original_subtree_nodes):
                original_node = original_subtree_nodes[i]
                if original_node in self._pt.nodes:
                    original_data = self._pt.items(original_node)
                    if original_data:
                        # Filter out instrument-related fields (handled separately above)
                        filtered_data = {k: v for k, v in original_data.items() 
                                       if not k.startswith('_') or k.startswith('_slur_')}
                        if filtered_data:
                            # Set the data on the corresponding new node
                            for key, value in filtered_data.items():
                                new_cu._pt.set_pfields(new_node, **{key: value})
        
        # Note: Envelopes that cross subtree boundaries are intentionally discarded
        # as per the design requirements.
        new_cu._envelopes = {}
        new_cu._next_envelope_id = 0
        
        return new_cu
    
    def copy(self):
        return self.from_subtree(self.rt.root)
