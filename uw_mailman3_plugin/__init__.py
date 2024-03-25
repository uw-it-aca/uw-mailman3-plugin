from public import public
from mailman.interfaces.plugin import IPlugin
from zope.interface import implementer


@public
@implementer(IPlugin)
class UWPlugin:
    def pre_hook(self):
        pass

    def post_hook(self):
        # uncomment to remove stock styles
        # manager = getUtility(IStyleManager)
        # manager.unregister(manager.get('legacy-announce'))
        # manager.unregister(manager.get('legacy-default'))
        # manager.unregister(manager.get('private-default'))
        pass

    @property
    def resource(self):
        return None
