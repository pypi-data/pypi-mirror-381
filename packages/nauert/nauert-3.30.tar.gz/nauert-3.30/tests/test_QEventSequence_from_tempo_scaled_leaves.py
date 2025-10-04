import abjad

import nauert


def test_QEventSequence_from_tempo_scaled_leaves_01():
    staff = abjad.Staff("c'4 r4 r8 cs'8 cs'8 d'8 d'8 ef'8 s4 r4 ef'8")
    staff.append("<c' cs' e'>4")
    abjad.tie(staff[3:5])
    abjad.tie(staff[5:7])
    tempo = abjad.MetronomeMark(abjad.Duration(1, 4), 55)
    leaves = abjad.select.leaves(staff)
    q_events = nauert.QEventSequence.from_tempo_scaled_leaves(leaves, tempo)
    assert q_events == nauert.QEventSequence(
        (
            nauert.PitchedQEvent(
                abjad.duration.offset(0, 1), (abjad.NamedPitch("c'"),)
            ),
            nauert.SilentQEvent(abjad.duration.offset(12000, 11)),
            nauert.PitchedQEvent(
                abjad.duration.offset(30000, 11), (abjad.NamedPitch("cs'"),)
            ),
            nauert.PitchedQEvent(
                abjad.duration.offset(42000, 11), (abjad.NamedPitch("d'"),)
            ),
            nauert.PitchedQEvent(
                abjad.duration.offset(54000, 11), (abjad.NamedPitch("ef'"),)
            ),
            nauert.SilentQEvent(abjad.duration.offset(60000, 11)),
            nauert.PitchedQEvent(
                abjad.duration.offset(84000, 11), (abjad.NamedPitch("ef'"),)
            ),
            nauert.PitchedQEvent(
                abjad.duration.offset(90000, 11),
                (
                    abjad.NamedPitch("c'"),
                    abjad.NamedPitch("cs'"),
                    abjad.NamedPitch("e'"),
                ),
            ),
            nauert.TerminalQEvent(abjad.duration.offset(102000, 11)),
        )
    )


def test_QEventSequence_from_tempo_scaled_leaves_02():
    staff = abjad.Staff("c'4 r4 r8 cs'8 cs'8 d'8 d'8 ef'8 s4 r4 ef'8")
    staff.append("<c' cs' e'>4")
    abjad.tie(staff[3:5])
    abjad.tie(staff[5:7])
    tempo = abjad.MetronomeMark(abjad.Duration(1, 4), 58)
    abjad.attach(tempo, staff[0], context="Staff")
    tempo = abjad.MetronomeMark(abjad.Duration(1, 4), 77)
    abjad.attach(tempo, staff[9], context="Staff")
    leaves = abjad.select.leaves(staff)
    q_events = nauert.QEventSequence.from_tempo_scaled_leaves(leaves)
    assert q_events == nauert.QEventSequence(
        (
            nauert.PitchedQEvent(
                abjad.duration.offset(0, 1), (abjad.NamedPitch("c'"),)
            ),
            nauert.SilentQEvent(abjad.duration.offset(30000, 29)),
            nauert.PitchedQEvent(
                abjad.duration.offset(75000, 29), (abjad.NamedPitch("cs'"),)
            ),
            nauert.PitchedQEvent(
                abjad.duration.offset(105000, 29), (abjad.NamedPitch("d'"),)
            ),
            nauert.PitchedQEvent(
                abjad.duration.offset(135000, 29), (abjad.NamedPitch("ef'"),)
            ),
            nauert.SilentQEvent(abjad.duration.offset(150000, 29)),
            nauert.PitchedQEvent(
                abjad.duration.offset(15600000, 2233), (abjad.NamedPitch("ef'"),)
            ),
            nauert.PitchedQEvent(
                abjad.duration.offset(16470000, 2233),
                (
                    abjad.NamedPitch("c'"),
                    abjad.NamedPitch("cs'"),
                    abjad.NamedPitch("e'"),
                ),
            ),
            nauert.TerminalQEvent(abjad.duration.offset(18210000, 2233)),
        )
    )
