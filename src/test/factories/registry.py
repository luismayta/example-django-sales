#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.utils.module_loading import import_module


class Apps(object):

    CLASSES_FACTORIES = {
        'customuser.Myuser': {
            'module': 'test.factories.user',
            'class': 'UserFactory',
        },
    }

    @classmethod
    def get_factory(cls, factory_name):
        """
        Returns the factory matching the given factory_name.
        As a shortcut, this function also accepts a single argument.
        """
        attribs = cls.CLASSES_FACTORIES.get(factory_name, None)

        if not attribs:
            raise ValueError('No Existe El Value {0}'.format(factory_name))

        module = import_module(attribs.get('module'))

        return getattr(
            module,
            attribs.get('class')
        )
