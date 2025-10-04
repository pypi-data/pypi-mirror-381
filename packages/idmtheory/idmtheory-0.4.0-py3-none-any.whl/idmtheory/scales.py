"""
This module defines scales and some functions which can operate on scales.
"""

__author__ = "https://codeberg.org/decoherence"

from enum import Enum, IntEnum
from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from itertools import accumulate

from .chords import IDScaleDegree, IDChord, IDChordType, IDChordFlags, CHORD_TYPES
from .notes import note_name, note_to_note_value, normalize_note_value, normalize_note_values, note_values_to_note_names
from .tone_intervals import IDToneInterval, transpose_tone_intervals


class IDScaleIntervals(Enum):

    """Defines the intervals for the different scale genus."""
    DIATONIC = [
        IDToneInterval.R,
        IDToneInterval.M2,
        IDToneInterval.M3,
        IDToneInterval.P4,
        IDToneInterval.P5,
        IDToneInterval.M6,
        IDToneInterval.M7,
        IDToneInterval.O,
    ]
    """Defines the intervals for the natural major scale."""

    HARMONIC = [
        IDToneInterval.R,
        IDToneInterval.M2,
        IDToneInterval.m3,
        IDToneInterval.P4,
        IDToneInterval.P5,
        IDToneInterval.m6,
        IDToneInterval.M7,
        IDToneInterval.O,
    ]
    """Defines the intervals for the harmonic minor scale."""

    MELODIC = [
        IDToneInterval.R,
        IDToneInterval.M2,
        IDToneInterval.m3,
        IDToneInterval.P4,
        IDToneInterval.P5,
        IDToneInterval.M6,
        IDToneInterval.M7,
        IDToneInterval.O,
    ]
    """Defines the intervals for the melodic minor scale."""


class IDGenusType(IntEnum):
    """Defines available scale genus types."""
    DIATONIC = 0
    HARMONIC = 1
    MELODIC  = 2

@dataclass
class IDScaleGenus:
    type: IDGenusType
    name: str
    intervals: list[IDToneInterval]
    mode_names: dict[int, str]
    order: list[int]


SCALE_GENERA = {
    IDGenusType.DIATONIC:
    IDScaleGenus(
        IDGenusType.DIATONIC,
        "Diatonic",
        IDScaleIntervals.DIATONIC.value,
        {
            1: "Natural Major",
            2: "Dorian",
            3: "Phrygian",
            4: "Lydian",
            5: "Mixolydian",
            6: "Natural Minor",
            7: "Locrian",
        },
        [4, 1, 5, 2, 6, 3, 7],
    ),
    IDGenusType.HARMONIC:
    IDScaleGenus(
        IDGenusType.HARMONIC,
        "Harmonic",
        IDScaleIntervals.HARMONIC.value,
        {
            1: "Harmonic Minor",
            2: "Locrian Natural 6",
            3: "Major Augmented",
            4: "Ukrainian Dorian",
            5: "Phrygian Dominant",
            6: "Lydian Natural 2",
            7: "Super Locrian bb7",
        },
        [6, 3, 4, 1, 5, 2, 7],
    ),
    IDGenusType.MELODIC:
    IDScaleGenus(
        IDGenusType.MELODIC,
        "Melodic",
        IDScaleIntervals.MELODIC.value,
        {
            1: "Melodic Minor",
            2: "Dorian b6",
            3: "Lydian Augmented",
            4: "Lydian Dominant",
            5: "Mixolydian b6",
            6: "Locrian #2",
            7: "Super Locrian",
        },
        [3, 4, 1, 5, 2, 6, 7],
    ),
}


class IDScale:
    """Represents a scale which is defined by its tonic note and its intervals, e.g. C Natural Major."""

    def __init__(self, tonic: int | str, genus:IDGenusType = IDGenusType.DIATONIC, mode = 1) -> None:
        """
        Args:
            tonic: The root note name OR the root note value of the scale.
            genus: The IDGenusType defines the tone intervals to be used for the scale.
            mode: The mode of the scale (1-7).
        """

        self.set_tonic_note(tonic)
        self.set_mode(mode)
        self.set_genus(genus)


    def clone(self) -> 'IDScale':
        """Returns a deep copy of the chord."""
        return deepcopy(self)


    def contains(self, note_value: int) -> bool:
        """Tests if a given note value belongs to the scale."""
        return normalize_note_value(note_value) in normalize_note_values(self.note_values())
    

    def circle_of_2nds(self) -> list[IDChord]:
        """Returns the chords of the scale as a circle of 2nds - gives the same result as the triad_chords() method."""
        return self.triad_chords()


    def circle_of_3rds(self) -> list[IDChord]:
        """Returns the chords of the scale as a circle of 3rds."""
        return self._circle_of_nths(3)
    

    def circle_of_4ths(self) -> list[IDChord]:
        """Returns the chords of the scale as a circle of 4ths."""
        return self._circle_of_nths(4)
    

    def _circle_of_nths(self, n: int) -> list[IDChord]:
        result: list[IDChord] = []
        triad_chords = self.triad_chords() * 3

        for i in range(7):
            result.append(triad_chords[(n - 1) * i])

        return result


    def genus(self) -> int:
        return self._template.type
    
    def genus_name(self) -> str:
        """Returns the name of the genus of the scale, i.e. 'Diatonic', 'Harmonic' or 'Melodic'."""
        return self._template.name
    

    def mode_name(self) -> str:
        """Returns the name of the scale's mode. e.g. 'Natural Major' or 'Mixolydian'."""
        return self._template.mode_names[self._mode]


    def mode(self) -> int:
        """Returns the mode of the scale."""
        return self._mode


    def name(self, style="flat") -> str:
        """Returns the name of the scale, e.g. 'C Natural Major' or 'F Lydian'."""
        return note_name(self._tonic_note_value, style, include_octave=False) + " " + self.mode_name()


    def note_name_in_scale(self, note_value, style = "flat") -> str:
        """Returns the relative nota name of the scale for a given note value.
        
        The relative note name of the tonic of the scale is '1', the next note in the scale
        has the relative note name '2', etc. Chromatic notes (not in scale) are named e.g.
        'b1' or '#5'.

        Args:
            style (optional): 'flat' OR 'sharp', defines if 'b' or '#' shall be prioritized for chromatic notes.
        """
        sharp = (note_value - 1) % IDToneInterval.OCTAVE
        note = (note_value + 0) % IDToneInterval.OCTAVE
        flat = (note_value + 1) % IDToneInterval.OCTAVE

        normalized_scale_values = normalize_note_values(self.note_values())
        note_value_to_pos = {v: i + 1 for i, v in enumerate(normalized_scale_values)}

        if (note in normalized_scale_values):
            return str(note_value_to_pos[note])
    
        flat_in_scale = flat in normalized_scale_values
        flat_name = 'b' + str(note_value_to_pos[flat]) 

        sharp_in_scale = sharp in normalized_scale_values
        sharp_name = '#' + str(note_value_to_pos[sharp])

        if (flat_in_scale and sharp_in_scale):
            if (style == "flat"):
                return flat_name
            else:
                return sharp_name

        if (flat_in_scale):
            return flat_name
        
        if (sharp_in_scale):
            return sharp_name
        
        raise RuntimeError("Could not determine note name in scale!")



    def note_values(self, base_note_value = 0, include_perfect_octave = False):
        """Returns the note values from one octave of the scale.
        
        Args:
            base_note_value (optional): This must be a C-note value. The returned values of the scale
              will be greater than this C-note value but also as close as possible to this C-note value.
            include_perfect_octave (optional): Seven notes will be returned When this parameter is False.
              Eight notes will be returned when this parameter is True.
        
        Raises:
            ValueError if input conditions are not met.
        """
        if base_note_value % IDToneInterval.OCTAVE != 0:
            raise ValueError("The base note must be a C note!")

        # calculate interval step size for the current mode
        scale_steps = deque([b - a for a, b in zip(self._template.intervals[:-1], self._template.intervals[1:])])
        scale_steps.rotate(1 - self._mode)

        # calculate note values realtive to the tonic
        relative_note_values = [0, *accumulate(scale_steps)]
        note_values = [v + base_note_value + self._tonic_note_value for v in relative_note_values]

        if (not include_perfect_octave):
            note_values = note_values[:-1]

        return note_values


    def secondary_dominants(self) -> list[IDChord]:
        result: list[IDChord] = []
        triad_chords = self.triad_chords() * 2

        for i in range(7):
            chord = triad_chords[i + 4]
            chord.set_type(IDChordType.MAJOR)
            chord.set_flags(IDChordFlags.DOMINANT_7)
            result.append(chord)

        return result
        



    def set_mode(self, mode: int) -> None:
        """Sets the mode of the scale.
        
        Args:
            mode: The mode of the scale (1-7).
        """
        if (mode < 1 or mode > 7):
            raise ValueError("The mode must be in the interval 1-7!")

        self._mode = mode


    def set_genus(self, genus: IDGenusType) -> None:
        """Sets the genus of the scale.
        
        Args:
            genus: A value from IDGenusType, i.e. DIATONIC, HARMONIC or MELODIC.
        """
        self._template = SCALE_GENERA[genus]

        if not self._template:
            raise ValueError("Invalid scale genus!")
        

    def set_tonic_note(self, tonic: int | str) -> None:
        """Sets the tonic note of the scale."""
        self._tonic_note_value = note_to_note_value(tonic)

    
    def tonic_note_value(self) -> int:
        """Returns the tonic note of the scale."""
        return self._tonic_note_value


    def triad_chords(self) -> list[IDChord]:
        """Returns a list of the triad chords of the scale, e.g. C, Dm, Em, F, G, Am, Bdim for the C Diatonic Major scale"""
        result: list[IDChord] = []
        scale_note_values = self.note_values() + transpose_tone_intervals(self.note_values(), IDToneInterval.OCTAVE)

        for i, note in enumerate(self.note_values()):
            chord_note_values = [scale_note_values[i + IDScaleDegree.TONIC], 
                                 scale_note_values[i + IDScaleDegree.MEDIANT], 
                                 scale_note_values[i + IDScaleDegree.DOMINANT]]
            chord_tonic = chord_note_values[0]
            chord_intervals = transpose_tone_intervals(chord_note_values, -chord_tonic)

            for chord_type, chord_template in CHORD_TYPES.items():
                if chord_intervals == chord_template.intervals():
                    result.append(IDChord(chord_tonic, chord_type))


        return result


    def __str__(self) -> str:
        return self.name() + " [" + ", ".join(note_values_to_note_names(self.note_values())) + " ]"
    

    def __repr__(self) -> str:
        return self.__str__()
        
