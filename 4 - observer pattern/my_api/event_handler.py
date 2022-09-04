# the event system has a number of subscribers that
# subscribe for a different number of events and each item
# in the dictionary will be a list of subscribers that need to be
# notified every time that event occurs.
subscribers = dict()


def subscribe(event_type: str, fn):
    '''
    event_type - event name to which subscribers sign up for.
    fn - function that has to be added to the subscribers list.

    The only thing we have to do when we subscribe to an 
    event type is to check if there's already a list of that event type
    otherwiise we create it.
    '''
    #
    if not event_type in subscribers:
        subscribers[event_type] = []

    subscribers[event_type].append(fn)


def post_event(event_type: str, data):
    ''' 
    data - transmitted info event is posted.

    If the event doesn't exist the function doesn't do anything.
    Otherwise the data will be transmitted for each subscriber 
    function.

    '''
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)
