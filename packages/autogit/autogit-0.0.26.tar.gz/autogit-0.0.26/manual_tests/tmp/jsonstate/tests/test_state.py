from unittest.mock import MagicMock


def test_basic_usage_flow() -> None:
    """This example is provided in the README.md"""

    from jsonstate import State

    state = State(
        {
            'title': 'State Example',
            'profile': {
                'name': 'Foo',
            },
            'products': [
                {'name': 'Foo', 'description': 'Foo spam'},
                {'name': 'Bar', 'description': 'Bar spam'},
            ],
        }
    )
    # print_event = lambda **kwargs: print("Event", kwargs)
    print_event = MagicMock()

    state.callbacks(key='title').append(print_event)
    state['profile'].callbacks(key='name').append(print_event)
    state['products'].callbacks().append(print_event)

    # This statement updates the state and also invokes on_change callback:
    state['title'] = 'Eggs'
    # Event {'new_value': 'Eggs', 'old_value': 'State Example', 'action': 'update'}
    print_event.assert_called_once_with(
        new_value='Eggs', old_value='State Example', action='update'
    )
    print_event.reset_mock()

    # This statement updates the state and also invokes on_change callback:
    state['profile']['name'] = 'Spam'
    # Event {'new_value': 'Eggs', 'old_value': 'State Example', 'action': 'update'}
    print_event.assert_called_once_with(
        new_value='Spam', old_value='Foo', action='update'
    )
    print_event.reset_mock()

    # This statement also updates the state and invokes on_change callback:
    state['products'].append({'name': 'Eggs', 'description': 'Eggs spam'})
    # Event {'new_value': {"name": "Eggs", "description": "Eggs spam"}, 'action': 'append'}

    ## TODO:
    print_event.assert_called_once_with(
        new_value={'name': 'Eggs', 'description': 'Eggs spam'}, action='add'
    )
    # Event {"new_value": {"name": "Eggs", "description": "Eggs spam"}, "action": "add"}
    print_event.reset_mock()
