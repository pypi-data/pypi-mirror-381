from unittest.mock import MagicMock, call

from jsonstate import State


def test_callback_for_list_methods_at_root_level() -> None:
    """
    Test observer callback invocations for these List methods:
    '__delitem__',
    '__reversed__',
    '__setitem__',
    'append',
    'clear',
    'copy',
    'extend',
    'insert',
    'pop',
    'remove',
    'reverse',
    'sort'
    """
    state_change_observer = MagicMock()

    state = State(['foo', 'bar'])
    assert state
    assert state[0] == 'foo'
    assert state[1] == 'bar'

    state.callbacks().append(state_change_observer)
    assert state_change_observer in state.callbacks()

    state.append('spam')
    assert 'spam' in state
    state_change_observer.assert_called_once_with(new_value='spam', action='add')
    state_change_observer.reset_mock()

    state[-1] = 'eggs'
    assert 'eggs' in state
    state_change_observer.assert_called_once_with(
        new_value='eggs', old_value='spam', action='update'
    )
    state_change_observer.reset_mock()

    assert 'eggs' in state
    del state[-1]
    state_change_observer.assert_called_once_with(old_value='eggs', action='remove')
    state_change_observer.reset_mock()

    assert 'bar' in state
    state.pop()
    state_change_observer.assert_called_once_with(old_value='bar', action='remove')
    state_change_observer.reset_mock()

    state.extend(['bar', 'spam'])
    state_change_observer.assert_has_calls(
        [call(new_value='bar', action='add'), call(new_value='spam', action='add')]
    )
    state_change_observer.reset_mock()

    state.insert(0, 'FOO')
    assert 'FOO' in state
    state_change_observer.assert_called_once_with(
        new_value='FOO', action='add', index=0
    )
    state_change_observer.reset_mock()

    state.remove('FOO')
    assert 'FOO' not in state
    state_change_observer.assert_called_once_with(old_value='FOO', action='remove')
    state_change_observer.reset_mock()

    state.clear()
    assert state == []
    state_change_observer.assert_has_calls(
        [
            call(old_value='foo', action='remove'),
            call(old_value='bar', action='remove'),
            call(old_value='spam', action='remove'),
        ]
    )
    state_change_observer.reset_mock()


def test_callback_for_list_methods_at_nested_level() -> None:
    state_change_observer = MagicMock()

    state = State(['foo', ['bar']])

    state[1].callbacks().append(state_change_observer)
    assert state_change_observer in state[1].callbacks()

    state[1].append('spam')
    state_change_observer.assert_called_once_with(new_value='spam', action='add')
    state_change_observer.reset_mock()
