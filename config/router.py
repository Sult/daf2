#create database router to destinguish between dynamic and static dataz
class Router(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'static':
            return 'static'
        elif model._meta.app_label == 'bulk':
            return 'bulk'
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'static':
            return 'static'
        elif model._meta.app_label == 'bulk':
            return 'bulk'
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, model):
        if db == 'static':
            return model._meta.app_label == 'static'
        elif db == 'bulk':
            return model._meta.app_label == 'bulk'
        elif model._meta.app_label == 'static':
            return False
        elif model._meta.app_label == 'bulk':
            return False
        return True
