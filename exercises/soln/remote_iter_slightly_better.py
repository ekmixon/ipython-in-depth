from IPython import parallel

def remote_iterator(view, name):
    """Return an iterator on an object living on a remote engine."""
    it_name = f'_{name}_iter'
    view.execute(f'{it_name} = iter({name})', block=True)
    next_ref = parallel.Reference(f'{it_name}.next')
    while True:
        try:
            yield view.apply_sync(next_ref)
        # This causes the StopIteration exception to be raised.
        except parallel.RemoteError as e:
            if e.ename == 'StopIteration':
                raise StopIteration
            else:
                raise e
