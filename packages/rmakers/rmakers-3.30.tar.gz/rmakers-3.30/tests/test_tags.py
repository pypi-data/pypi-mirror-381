import abjad

import rmakers


def test_tags_01():
    """
    Tags work with ``rmakers.accelerando()``.
    """

    def make_lilypond_file(pairs):
        time_signatures = rmakers.time_signatures(pairs)
        durations = abjad.duration.durations(time_signatures)
        tag = abjad.Tag("ACCELERANDO_RHYTHM_MAKER")
        interpolation = rmakers.Interpolation(
            *abjad.duration.durations([(1, 8), (1, 20), (1, 16)])
        )
        tuplets = rmakers.accelerando(durations, [interpolation], tag=tag)
        lilypond_file = rmakers.example(tuplets, time_signatures)
        voice = lilypond_file["Voice"]
        rmakers.feather_beam(voice, tag=tag)
        rmakers.duration_bracket(voice)
        return lilypond_file

    pairs = [(4, 8), (3, 8), (4, 8), (3, 8)]
    lilypond_file = make_lilypond_file(pairs)
    string = abjad.lilypond(lilypond_file["Score"], tags=True)

    assert string == abjad.string.normalize(
        r"""
        \context Score = "Score"
        {
            \context RhythmicStaff = "Staff"
            \with
            {
                \override Clef.stencil = ##f
            }
            {
                \context Voice = "Voice"
                {
                    \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \rhythm { 2 }
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    \tuplet 1/1
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    {
                        \time 4/8
                        \once \override Beam.grow-direction = #right
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 63/32
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.feather_beam()
                        [
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 115/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 91/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 35/32
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 29/32
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 13/16
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.feather_beam()
                        ]
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    }
                    \revert TupletNumber.text
                    \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \rhythm { 4. }
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    \tuplet 1/1
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    {
                        \time 3/8
                        \once \override Beam.grow-direction = #right
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 117/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.feather_beam()
                        [
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 99/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 69/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 13/16
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 47/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.feather_beam()
                        ]
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    }
                    \revert TupletNumber.text
                    \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \rhythm { 2 }
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    \tuplet 1/1
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    {
                        \time 4/8
                        \once \override Beam.grow-direction = #right
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 63/32
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.feather_beam()
                        [
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 115/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 91/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 35/32
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 29/32
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 13/16
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.feather_beam()
                        ]
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    }
                    \revert TupletNumber.text
                    \override TupletNumber.text = \markup \scale #'(0.75 . 0.75) \rhythm { 4. }
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    \tuplet 1/1
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    {
                        \time 3/8
                        \once \override Beam.grow-direction = #right
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 117/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.feather_beam()
                        [
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 99/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 69/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 13/16
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.accelerando()
                        c'16 * 47/64
                          %! ACCELERANDO_RHYTHM_MAKER
                          %! rmakers.feather_beam()
                        ]
                      %! ACCELERANDO_RHYTHM_MAKER
                      %! rmakers.accelerando()
                    }
                    \revert TupletNumber.text
                }
            }
        }
        """
    )


def test_tags_02():
    """
    Tags work with rmakers.incised().
    """

    def make_lilypond_file(pairs):
        tag = abjad.Tag("INCISED_RHYTHM_MAKER")
        time_signatures = rmakers.time_signatures(pairs)
        durations = abjad.duration.durations(time_signatures)
        tuplets = rmakers.incised(
            durations,
            extra_counts=[1],
            outer_tuplets_only=True,
            prefix_talea=[-1],
            prefix_counts=[1],
            suffix_talea=[-1],
            suffix_counts=[1],
            talea_denominator=8,
            tag=tag,
        )
        container = abjad.Container(tuplets)
        rmakers.force_augmentation(container)
        rmakers.beam(container, tag=tag)
        rmakers.tweak_tuplet_number_text_calc_fraction_text(container)
        components = abjad.mutate.eject_contents(container)
        lilypond_file = rmakers.example(components, time_signatures)
        return lilypond_file

    pairs = [(8, 8), (4, 8), (6, 8)]
    lilypond_file = make_lilypond_file(pairs)
    string = abjad.lilypond(lilypond_file["Score"], tags=True)

    assert string == abjad.string.normalize(
        r"""
        \context Score = "Score"
        {
            \context RhythmicStaff = "Staff"
            \with
            {
                \override Clef.stencil = ##f
            }
            {
                \context Voice = "Voice"
                {
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    \tweak text #tuplet-number::calc-fraction-text
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    \tuplet 9/16
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    {
                        \time 8/8
                          %! INCISED_RHYTHM_MAKER
                          %! rmakers.incised()
                        r16
                          %! INCISED_RHYTHM_MAKER
                          %! rmakers.incised()
                        c'2
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    }
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    \tweak text #tuplet-number::calc-fraction-text
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    \tuplet 5/8
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    {
                        \time 4/8
                          %! INCISED_RHYTHM_MAKER
                          %! rmakers.incised()
                        c'4
                        ~
                          %! INCISED_RHYTHM_MAKER
                          %! rmakers.incised()
                        c'16
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    }
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    \tweak text #tuplet-number::calc-fraction-text
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    \tuplet 7/12
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    {
                        \time 6/8
                          %! INCISED_RHYTHM_MAKER
                          %! rmakers.incised()
                        c'4.
                          %! INCISED_RHYTHM_MAKER
                          %! rmakers.incised()
                        r16
                      %! INCISED_RHYTHM_MAKER
                      %! rmakers.incised()
                    }
                }
            }
        }
        """
    )


def test_tags_03():
    """
    Tags work with rmakers.talea().
    """

    def make_lilypond_file(pairs):
        time_signatures = rmakers.time_signatures(pairs)
        durations = abjad.duration.durations(time_signatures)
        tag = abjad.Tag("TALEA_RHYTHM_MAKER")
        tuplets = rmakers.talea(
            durations, [1, 2, 3, 4], 16, extra_counts=[0, 1], tag=tag
        )
        rmakers.tweak_tuplet_number_text_calc_fraction_text(tuplets)
        lilypond_file = rmakers.example(tuplets, time_signatures)
        voice = lilypond_file["Voice"]
        rmakers.beam(voice, tag=tag)
        return lilypond_file

    pairs = [(3, 8), (4, 8), (3, 8), (4, 8)]
    lilypond_file = make_lilypond_file(pairs)
    string = abjad.lilypond(lilypond_file["Score"], tags=True)

    assert string == abjad.string.normalize(
        r"""
        \context Score = "Score"
        {
            \context RhythmicStaff = "Staff"
            \with
            {
                \override Clef.stencil = ##f
            }
            {
                \context Voice = "Voice"
                {
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    \tweak text #tuplet-number::calc-fraction-text
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    \tuplet 1/1
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    {
                        \time 3/8
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'16
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.beam()
                        [
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'8
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'8.
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.beam()
                        ]
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    }
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    \tuplet 9/8
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    {
                        \time 4/8
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'4
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'16
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.beam()
                        [
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'8
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'8
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.beam()
                        ]
                        ~
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    }
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    \tweak text #tuplet-number::calc-fraction-text
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    \tuplet 1/1
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    {
                        \time 3/8
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'16
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'4
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'16
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    }
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    \tuplet 9/8
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    {
                        \time 4/8
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'8
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.beam()
                        [
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'8.
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.beam()
                        ]
                          %! TALEA_RHYTHM_MAKER
                          %! rmakers.talea()
                        c'4
                      %! TALEA_RHYTHM_MAKER
                      %! rmakers.talea()
                    }
                }
            }
        }
        """
    )


def test_tags_04():
    """
    Tags work with rmakers.tuplet().
    """

    """
    def make_lilypond_file(pairs):
        time_signatures = rmakers.time_signatures(pairs)
        durations = abjad.duration.durations(time_signatures)
        tag = abjad.Tag("TALEA_RHYTHM_MAKER")
        tuplets = rmakers.talea(
            durations, [1, 2, 3, 4], 16, extra_counts=[0, 1], tag=tag
        )
        rmakers.tweak_tuplet_number_text_calc_fraction_text(tuplets)
        lilypond_file = rmakers.example(tuplets, time_signatures)
        voice = lilypond_file["Voice"]
        rmakers.beam(voice, tag=tag)
        return lilypond_file

    pairs = [(3, 8), (4, 8), (3, 8), (4, 8)]
    lilypond_file = make_lilypond_file(pairs)
    string = abjad.lilypond(lilypond_file["Score"], tags=True)
    """

    def make_lilypond_file(pairs):
        time_signatures = rmakers.time_signatures(pairs)
        durations = abjad.duration.durations(time_signatures)
        tag = abjad.Tag("TUPLET_RHYTHM_MAKER")
        tuplets = rmakers.tuplet(durations, [(3, 2)], tag=tag)
        rmakers.tweak_tuplet_number_text_calc_fraction_text(tuplets)
        lilypond_file = rmakers.example(tuplets, time_signatures)
        voice = lilypond_file["Voice"]
        rmakers.beam(voice, tag=tag)
        return lilypond_file

    pairs = [(1, 2), (3, 8), (5, 16), (5, 16)]
    lilypond_file = make_lilypond_file(pairs)
    string = abjad.lilypond(lilypond_file["Score"], tags=True)

    assert string == abjad.string.normalize(
        r"""
        \context Score = "Score"
        {
            \context RhythmicStaff = "Staff"
            \with
            {
                \override Clef.stencil = ##f
            }
            {
                \context Voice = "Voice"
                {
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    \tuplet 5/4
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    {
                        \time 1/2
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.tuplet()
                        c'4.
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.tuplet()
                        c'4
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    }
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    \tweak text #tuplet-number::calc-fraction-text
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    \tuplet 5/3
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    {
                        \time 3/8
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.tuplet()
                        c'4.
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.tuplet()
                        c'4
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    }
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    \tweak text #tuplet-number::calc-fraction-text
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    \tuplet 1/1
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    {
                        \time 5/16
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.tuplet()
                        c'8.
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.beam()
                        [
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.tuplet()
                        c'8
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.beam()
                        ]
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    }
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    \tweak text #tuplet-number::calc-fraction-text
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    \tuplet 1/1
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    {
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.tuplet()
                        c'8.
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.beam()
                        [
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.tuplet()
                        c'8
                          %! TUPLET_RHYTHM_MAKER
                          %! rmakers.beam()
                        ]
                      %! TUPLET_RHYTHM_MAKER
                      %! rmakers.tuplet()
                    }
                }
            }
        }
        """
    )
