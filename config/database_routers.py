
#create database router to destinguish between dynamic and static dataz
class StaticRouter(object):
    """
    A router to control all database operations on models in the
    static application.
    """
    
    def db_for_read(self, model, **hints):
        """Attempts to read static models go to static."""
        if model._meta.app_label == 'static':
            return 'static'
        return None


    def db_for_write(self, model, **hints):
        """Attempts to write auth models go to static."""
        if model._meta.app_label == 'static':
            return 'static'
        return None


    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the static app is involved."""
        if obj1._meta.app_label != 'static' and obj2._meta.app_label != 'static':
            return True
        return None


    def allow_migrate(self, db, model):
        """Make sure the static app only appears in the 'static' database."""
        if db == 'static':
            return model._meta.app_label == 'static'
        elif model._meta.app_label == 'static':
            return True
        return None
    

#create database router to destinguish between dynamic and bulk dataz
class BulkRouter(object):
    """
    A router to control all database operations on models in the
    bulk application.
    """
    
    def db_for_read(self, model, **hints):
        """Attempts to read bulk models go to bulk."""
        if model._meta.app_label == 'bulk':
            return 'bulk'
        return None


    def db_for_write(self, model, **hints):
        """Attempts to write auth models go to bulk."""
        if model._meta.app_label == 'bulk':
            return 'bulk'
        return None


    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in the bulk app is involved."""
        if obj1._meta.app_label != 'bulk' and obj2._meta.app_label != 'bulk':
            return True
        return None


    def allow_migrate(self, db, model):
        """Make sure the bulk app only appears in the 'bulk' database."""
        if db == 'bulk':
            return model._meta.app_label == 'bulk'
        elif model._meta.app_label == 'bulk':
            return True
        return None


class DefaultRouter(object):
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen slave.
        """
        return "default"

    def db_for_write(self, model, **hints):
        """
        Writes always go to master.
        """
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.
        """
        return True

    def allow_migrate(self, db, model):
        """
        All non-auth models end up in this pool.
        """
        return True
