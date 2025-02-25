"""Application middleware."""

import pynecone as pc


class CloseSidebarMiddleware(pc.Middleware):
    """Middleware to make sure the sidebar closes when the page changes."""

    def preprocess(self, app, state, event):
        """Preprocess the event.

        Args:
            app: The app to apply the middleware to.
            state: The client state.
            event: The event to preprocess.
        """
        if event.name == pc.event.get_hydrate_event(state):
            state.get_substate(["navbar_state"]).sidebar_open = False
            state.get_substate(["index_state"]).show_c2a = True
