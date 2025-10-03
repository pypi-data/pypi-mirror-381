from datetime import datetime
from unittest.mock import MagicMock

import pytest

from jsonstate import State


@pytest.mark.parametrize(
    ('state_name', 'initial_value', 'new_value'),
    [
        # String
        ('title', 'Initial title', 'Updated title'),
        ## list
        ('tags', ['Foo', 'Bar'], ['Eggs', 'Spam']),
        ## tuple
        ('tags', ('Foo', 'Bar'), ('Eggs', 'Spam')),
        ## dict
        ('metrics', {'speed': 1, 'excitment': 9}, {'saved_time': 99, 'joy': 99}),
        ## bool
        ('dark', False, True),
        ## int
        ('opacity', 99, 0),
        ## float
        ('value', 1.5, 79.8),
        ## datetime
        ('now', datetime(2025, 1, 30), datetime(2025, 2, 28)),
    ],
)
def test_state_observer_in_top_level(state_name, initial_value, new_value) -> None:
    """
    Test possible actions on top level keys.

    Interface of possible actions: (keyword only arguments)
    - action="add" new_value=<value>
    - action="update" old_value=<value>, new_value=<value>
    - action="remove" old_value=<value>
    """
    state_change_observer = MagicMock()

    state = State({state_name: initial_value})
    assert state
    assert state[state_name] == initial_value

    state.callbacks(key=state_name).append(
        state_change_observer
    )  # .on_change = state_change_observer
    assert state_change_observer in state.callbacks(key=state_name)

    state.pop(state_name)
    state_change_observer.assert_called_once_with(
        old_value=initial_value, action='remove'
    )
    state_change_observer.reset_mock()

    state[state_name] = initial_value
    state_change_observer.assert_called_once_with(new_value=initial_value, action='add')
    state_change_observer.reset_mock()

    state[state_name] = new_value
    state_change_observer.assert_called_once_with(
        new_value=new_value, old_value=initial_value, action='update'
    )
    state_change_observer.reset_mock()


def test_callback_for_dict_methods_at_the_top_level() -> None:
    """
    Test observer callback invocations for these Dict methods:
     - __setitem__
     - __delitem__
     - pop
     - popitem
     - clear
     - update - dict
     - update - iterable
     - update - kwargs
     - setdefault
    """
    state_change_observer = MagicMock()

    state = State({'foo': 'bar'})
    assert state
    assert state['foo'] == 'bar'

    state.callbacks(key='foo').append(
        state_change_observer
    )  # .on_change = state_change_observer
    assert state_change_observer in state.callbacks(key='foo')

    state = State({'foo': 'bar'})
    state.callbacks(key='foo').append(state_change_observer)
    state['foo'] = 'spam'
    state_change_observer.assert_called_once_with(
        new_value='spam', old_value='bar', action='update'
    )
    state_change_observer.reset_mock()

    state = State({'foo': 'bar'})
    state.callbacks(key='foo').append(state_change_observer)
    del state['foo']
    state_change_observer.assert_called_once_with(old_value='bar', action='remove')
    state_change_observer.reset_mock()

    state = State({'foo': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.pop('foo')
    state_change_observer.assert_called_once_with(old_value='spam', action='remove')
    state_change_observer.reset_mock()

    state = State({'foo': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.popitem()
    state_change_observer.assert_called_once_with(old_value='spam', action='remove')
    state_change_observer.reset_mock()

    state = State({'foo': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.clear()
    state_change_observer.assert_called_once_with(old_value='spam', action='remove')
    state_change_observer.reset_mock()

    # Update Dict: value gets updated
    state = State({'foo': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update({'foo': 'eggs'})
    state_change_observer.assert_called_once_with(
        new_value='eggs', old_value='spam', action='update'
    )
    state_change_observer.reset_mock()

    # Update Dict: value does not get updated
    state = State({'bar': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update({'foo': 'eggs'})
    state_change_observer.assert_called_once_with(new_value='eggs', action='add')
    state_change_observer.reset_mock()

    # Update Iterable: value gets updated
    state = State({'foo': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update([('foo', 'eggs')])
    state_change_observer.assert_called_once_with(
        new_value='eggs', old_value='spam', action='update'
    )
    state_change_observer.reset_mock()

    # Update Iterable: value does not get updated
    state = State({'bar': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update([('foo', 'eggs')])
    state_change_observer.assert_called_once_with(new_value='eggs', action='add')
    state_change_observer.reset_mock()

    # Update Kwargs: value gets updated
    state = State({'foo': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update(foo='eggs')
    state_change_observer.assert_called_once_with(
        new_value='eggs', old_value='spam', action='update'
    )
    state_change_observer.reset_mock()

    # Update Kwargs: value does not get updated
    state = State({'bar': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update(foo='eggs')
    state_change_observer.assert_called_once_with(new_value='eggs', action='add')
    state_change_observer.reset_mock()

    state = State({'foo': 'spam'})
    state.callbacks(key='foo').append(state_change_observer)
    state.setdefault('foo', 'eggs')
    state_change_observer.assert_not_called()
    state_change_observer.reset_mock()

    state = State({})
    state.callbacks(key='foo').append(state_change_observer)
    state.setdefault('foo', 'eggs')
    state_change_observer.assert_called_once_with(new_value='eggs', action='add')
    state_change_observer.reset_mock()


def test_update_is_not_sent_if_old_value_matches_new_one() -> None:
    """
    - __setitem__
    - __delitem__
    - pop
    - popitem
    - clear
    - update - dict
    - update - iterable
    - update - kwargs
    - setdefault
    """
    state_change_observer = MagicMock()

    state = State({'foo': 'bar'})
    state.callbacks(key='foo').append(state_change_observer)
    state['foo'] = 'bar'
    state_change_observer.assert_not_called()
    state_change_observer.reset_mock()

    # # Dict
    state = State({'foo': 'bar'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update({'foo': 'bar'})
    state_change_observer.assert_not_called()
    state_change_observer.reset_mock()

    # # Iterable
    state = State({'foo': 'bar'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update([('foo', 'bar')])
    state_change_observer.assert_not_called()
    state_change_observer.reset_mock()

    # # Kwargs
    state = State({'foo': 'bar'})
    state.callbacks(key='foo').append(state_change_observer)
    state.update(foo='bar')
    state_change_observer.assert_not_called()
    state_change_observer.reset_mock()


def test_nested_dict_observation() -> None:
    state_change_observer = MagicMock()
    state = State(
        {
            'foo': {'bar': 'spam'},
        }
    )
    state['foo'].callbacks(key='bar').append(state_change_observer)
    state['foo']['bar'] = 'eggs'

    state_change_observer.assert_called_once_with(
        new_value='eggs', old_value='spam', action='update'
    )
    state_change_observer.reset_mock()

    # 3 level nesting
    state_change_observer = MagicMock()
    state = State(
        {
            'one': {'two': {'three': 'four'}},
        }
    )
    state['one']['two'].callbacks(key='three').append(state_change_observer)
    state['one']['two']['three'] = 'five'

    state_change_observer.assert_called_once_with(
        new_value='five', old_value='four', action='update'
    )
    state_change_observer.reset_mock()


def test_add_callback_for_non_existing_key() -> None:
    state_change_observer = MagicMock()
    state = State(
        {
            'foo': {'bar': 'spam'},
        }
    )
    state['foo'].callbacks(key='bar').append(state_change_observer)
    state['foo']['bar'] = 'eggs'

    state_change_observer.assert_called_once_with(
        new_value='eggs', old_value='spam', action='update'
    )
    state_change_observer.reset_mock()

    # 3 level nesting
    state_change_observer = MagicMock()
    state = State(
        {
            'one': {'two': {'three': 'four'}},
        }
    )
    state['one'].callbacks(key='three').append(state_change_observer)
    state['one']['three'] = 'five'

    state_change_observer.assert_called_once_with(new_value='five', action='add')
    state_change_observer.reset_mock()
