# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025-08-22 13:45:58
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Database config methods.
"""


from typing import Any, TypedDict, TypeVar, Generic
from datetime import (
    datetime as Datetime,
    date as Date,
    time as Time,
    timedelta as Timedelta
)
from reykit.rbase import Null, throw

from . import rdb
from . import rorm
from .rbase import DatabaseBase


__all__ = (
    'DatabaseTableConfig',
    'DatabaseConfigSuper',
    'DatabaseConfig',
    'DatabaseConfigAsync'
)


type ConfigValue = bool | str | int | float | list | tuple | dict | set | Datetime | Date | Time | Timedelta | None
ConfigRow = TypedDict('ConfigRow', {'key': str, 'value': ConfigValue, 'type': str, 'note': str | None})
type ConfigTable = list[ConfigRow]
ConfigValueT = TypeVar('T', bound=ConfigValue) # Any.
DatabaseT = TypeVar('DatabaseT', 'rdb.Database', 'rdb.DatabaseAsync')


class DatabaseTableConfig(rorm.Model, table=True):
    """
    Database `config` table model.
    """

    __comment__ = 'Config data table.'
    create_time: rorm.Datetime = rorm.Field(field_default=':create_time', not_null=True, index_n=True, comment='Config create time.')
    update_time: rorm.Datetime = rorm.Field(field_default=':update_time', index_n=True, comment='Config update time.')
    key: str = rorm.Field(rorm.types.VARCHAR(50), key=True, comment='Config key.')
    value: str = rorm.Field(rorm.types.TEXT, not_null=True, comment='Config value.')
    type: str = rorm.Field(rorm.types.VARCHAR(50), not_null=True, comment='Config value type.')
    note: str = rorm.Field(rorm.types.VARCHAR(500), comment='Config note.')


class DatabaseConfigSuper(DatabaseBase, Generic[DatabaseT]):
    """
    Database config super type.
    Can create database used `self.build_db` method.

    Attributes
    ----------
    db_names : Database table name mapping dictionary.
    """

    db_names = {
        'config': 'config',
        'stats_config': 'stats_config'
    }


    def __init__(self, db: DatabaseT) -> None:
        """
        Build instance attributes.

        Parameters
        ----------
        db: Database instance.
        """

        # Build.
        self.db = db


    def handle_build_db(self) -> tuple[list[type[DatabaseTableConfig]], list[dict[str, Any]]] :
        """
        Handle method of check and build database tables, by `self.db_names`.

        Returns
        -------
        Build database parameter.
        """

        # Set parameter.

        ## Table.
        DatabaseTableConfig._set_name(self.db_names['config'])
        tables = [DatabaseTableConfig]

        ## View stats.
        views_stats = [
            {
                'path': self.db_names['stats_config'],
                'items': [
                    {
                        'name': 'count',
                        'select': (
                            'SELECT COUNT(1)\n'
                            f'FROM `{self.db.database}`.`{self.db_names['config']}`'
                        ),
                        'comment': 'Config count.'
                    },
                    {
                        'name': 'last_create_time',
                        'select': (
                            'SELECT MAX(`create_time`)\n'
                            f'FROM `{self.db.database}`.`{self.db_names['config']}`'
                        ),
                        'comment': 'Config last record create time.'
                    },
                    {
                        'name': 'last_update_time',
                        'select': (
                            'SELECT MAX(`update_time`)\n'
                            f'FROM `{self.db.database}`.`{self.db_names['config']}`'
                        ),
                        'comment': 'Config last record update time.'
                    }
                ]
            }
        ]

        return tables, views_stats


class DatabaseConfig(DatabaseConfigSuper['rdb.Database']):
    """
    Database config type.
    Can create database used `self.build_db` method.

    Examples
    --------
    >>> config = DatabaseConfig()
    >>> config['key1'] = 1
    >>> config['key2', 'note'] = 2
    >>> config['key1'], config['key2']
    (1, 2)
    """


    def build_db(self) -> None:
        """
        Check and build database tables, by `self.db_names`.
        """

        # Set parameter.
        tables, views_stats = self.handle_build_db()

        # Build.
        self.db.build.build(tables=tables, views_stats=views_stats, skip=True)


    def data(self) -> ConfigTable:
        """
        Get config data table.

        Returns
        -------
        Config data table.
        """

        # Get.
        result = self.db.execute.select(
            self.db_names['config'],
            ['key', 'value', 'type', 'note'],
            order='IFNULL(`update_time`, `create_time`) DESC'
        )

        # Convert.
        global_dict = {'datetime': Datetime}
        result = [
            {
                'key': row['key'],
                'value': eval(row['value'], global_dict),
                'note': row['note']
            }
            for row in result
        ]

        return result


    def get(self, key: str, default: ConfigValueT | None = None) -> ConfigValue | ConfigValueT:
        """
        Get config value, when not exist, then return default value.

        Parameters
        ----------
        key : Config key.
        default : Config default value.

        Returns
        -------
        Config value.
        """

        # Get.
        where = '`key` = :key'
        result = self.db.execute.select(
            self.db_names['config'],
            '`value`',
            where,
            limit=1,
            key=key
        )
        value = result.scalar()

        # Default.
        if value is None:
            value = default
        else:
            global_dict = {'datetime': Datetime}
            value = eval(value, global_dict)

        return value


    def setdefault(
        self,
        key: str,
        default: ConfigValueT | None = None,
        default_note: str | None = None
    ) -> ConfigValue | ConfigValueT:
        """
        Set config default value.

        Parameters
        ----------
        key : Config key.
        default : Config default value.
        default_note : Config default note.

        Returns
        -------
        Config value.
        """

        # Set.
        data = {
            'key': key,
            'value': repr(default),
            'type': type(default).__name__,
            'note': default_note
        }
        result = self.db.execute.insert(
            self.db_names['config'],
            data,
            'ignore'
        )

        # Get.
        if result.rowcount == 0:
            default = self.get(key)

        return default


    def update(self, data: dict[str, ConfigValue] | ConfigTable) -> None:
        """
        Update config values.

        Parameters
        ----------
        data : Config update data.
            - `dict[str, Any]`: Config key and value.
            - `ConfigTable`: Config key and value and note.
        """

        # Set parameter.
        if type(data) == dict:
            data = [
                {
                    'key': key,
                    'value': repr(value),
                    'type': type(value).__name__
                }
                for key, value in data.items()
            ]
        else:
            data = data.copy()
            for row in data:
                row['value'] = repr(row['value'])
                row['type'] = type(row['value']).__name__

        # Update.
        self.db.execute.insert(
            self.db_names['config'],
            data,
            'update'
        )


    def remove(self, key: str | list[str]) -> None:
        """
        Remove config.

        Parameters
        ----------
        key : Config key or key list.
        """

        # Remove.
        if type(key) == str:
            where = '`key` = :key'
            limit = 1
        else:
            where = '`key` in :key'
            limit = None
        result = self.db.execute.delete(
            self.db_names['base.config'],
            where,
            limit=limit,
            key=key
        )

        # Check.
        if result.rowcount == 0:
            throw(KeyError, key)


    def items(self) -> dict[str, ConfigValue]:
        """
        Get all config keys and values.

        Returns
        -------
        All config keys and values.
        """

        # Get.
        result = self.db.execute.select(
            self.db_names['config'],
            ['key', 'value']
        )

        # Convert.
        global_dict = {'datetime': Datetime}
        result = result.to_dict('key', 'value')
        result = {
            key: eval(value, global_dict)
            for key, value in result.items()
        }

        return result


    def keys(self) -> list[str]:
        """
        Get all config keys.

        Returns
        -------
        All config keys.
        """

        # Get.
        result = self.db.execute.select(
            self.db_names['config'],
            '`key`'
        )

        # Convert.
        global_dict = {'datetime': Datetime}
        result = [
            eval(value, global_dict)
            for value in result
        ]

        return result


    def values(self) -> list[ConfigValue]:
        """
        Get all config value.

        Returns
        -------
        All config values.
        """

        # Get.
        result = self.db.execute.select(
            self.db_names['config'],
            '`value`'
        )

        # Convert.
        global_dict = {'datetime': Datetime}
        result = [
            eval(value, global_dict)
            for value in result
        ]

        return result


    def __getitem__(self, key: str) -> ConfigValue:
        """
        Get config value.

        Parameters
        ----------
        key : Config key.

        Returns
        -------
        Config value.
        """

        # Get.
        value = self.get(key, Null)

        # Check.
        if value == Null:
            throw(KeyError, key)

        return value


    def __setitem__(self, key_note: str | tuple[str, str], value: ConfigValue) -> None:
        """
        Set config value.

        Parameters
        ----------
        key_note : Config key and note.
        value : Config value.
        """

        # Set parameter.
        if type(key_note) != str:
            key, note = key_note
        else:
            key = key_note
            note = None

        # Set.
        data = {
            'key': key,
            'value': repr(value),
            'type': type(value).__name__,
            'note': note
        }
        self.db.execute.insert(
            self.db_names['config'],
            data,
            'update'
        )


class DatabaseConfigAsync(DatabaseConfigSuper['rdb.DatabaseAsync']):
    """
    Asynchronous database config type.
    Can create database used `self.build_db` method.

    Examples
    --------
    >>> config = DatabaseConfig()
    >>> await config['key1'] = 1
    >>> await config['key2', 'note'] = 2
    >>> await config['key1'], config['key2']
    (1, 2)
    """


    async def build_db(self) -> None:
        """
        Asynchronous check and build database tables, by `self.db_names`.
        """

        # Set parameter.
        tables, views_stats = self.handle_build_db()

        # Build.
        await self.db.build.build(tables=tables, views_stats=views_stats, skip=True)


    async def data(self) -> ConfigTable:
        """
        Asynchronous get config data table.

        Returns
        -------
        Config data table.
        """

        # Get.
        result = await self.db.execute.select(
            self.db_names['config'],
            ['key', 'value', 'type', 'note'],
            order='IFNULL(`update_time`, `create_time`) DESC'
        )

        # Convert.
        global_dict = {'datetime': Datetime}
        result = [
            {
                'key': row['key'],
                'value': eval(row['value'], global_dict),
                'note': row['note']
            }
            for row in result
        ]

        return result


    async def get(self, key: str, default: ConfigValueT | None = None) -> ConfigValue | ConfigValueT:
        """
        Asynchronous get config value, when not exist, then return default value.

        Parameters
        ----------
        key : Config key.
        default : Config default value.

        Returns
        -------
        Config value.
        """

        # Get.
        where = '`key` = :key'
        result = await self.db.execute.select(
            self.db_names['config'],
            '`value`',
            where,
            limit=1,
            key=key
        )
        value = result.scalar()

        # Default.
        if value is None:
            value = default
        else:
            global_dict = {'datetime': Datetime}
            value = eval(value, global_dict)

        return value


    async def setdefault(
        self,
        key: str,
        default: ConfigValueT | None = None,
        default_note: str | None = None
    ) -> ConfigValue | ConfigValueT:
        """
        Asynchronous set config default value.

        Parameters
        ----------
        key : Config key.
        default : Config default value.
        default_note : Config default note.

        Returns
        -------
        Config value.
        """

        # Set.
        data = {
            'key': key,
            'value': repr(default),
            'type': type(default).__name__,
            'note': default_note
        }
        result = await self.db.execute.insert(
            self.db_names['config'],
            data,
            'ignore'
        )

        # Get.
        if result.rowcount == 0:
            default = await self.get(key)

        return default


    async def update(self, data: dict[str, ConfigValue] | ConfigTable) -> None:
        """
        Asynchronous update config values.

        Parameters
        ----------
        data : Config update data.
            - `dict[str, Any]`: Config key and value.
            - `ConfigTable`: Config key and value and note.
        """

        # Set parameter.
        if type(data) == dict:
            data = [
                {
                    'key': key,
                    'value': repr(value),
                    'type': type(value).__name__
                }
                for key, value in data.items()
            ]
        else:
            data = data.copy()
            for row in data:
                row['value'] = repr(row['value'])
                row['type'] = type(row['value']).__name__

        # Update.
        await self.db.execute.insert(
            self.db_names['config'],
            data,
            'update'
        )


    async def remove(self, key: str | list[str]) -> None:
        """
        Asynchronous remove config.

        Parameters
        ----------
        key : Config key or key list.
        """

        # Remove.
        if type(key) == str:
            where = '`key` = :key'
            limit = 1
        else:
            where = '`key` in :key'
            limit = None
        result = await self.db.execute.delete(
            self.db_names['base.config'],
            where,
            limit=limit,
            key=key
        )

        # Check.
        if result.rowcount == 0:
            throw(KeyError, key)


    async def items(self) -> dict[str, ConfigValue]:
        """
        Asynchronous get all config keys and values.

        Returns
        -------
        All config keys and values.
        """

        # Get.
        result = await self.db.execute.select(
            self.db_names['config'],
            ['key', 'value']
        )

        # Convert.
        global_dict = {'datetime': Datetime}
        result = result.to_dict('key', 'value')
        result = {
            key: eval(value, global_dict)
            for key, value in result.items()
        }

        return result


    async def keys(self) -> list[str]:
        """
        Asynchronous get all config keys.

        Returns
        -------
        All config keys.
        """

        # Get.
        result = await self.db.execute.select(
            self.db_names['config'],
            '`key`'
        )

        # Convert.
        global_dict = {'datetime': Datetime}
        result = [
            eval(value, global_dict)
            for value in result
        ]

        return result


    async def values(self) -> list[ConfigValue]:
        """
        Asynchronous get all config value.

        Returns
        -------
        All config values.
        """

        # Get.
        result = await self.db.execute.select(
            self.db_names['config'],
            '`value`'
        )

        # Convert.
        global_dict = {'datetime': Datetime}
        result = [
            eval(value, global_dict)
            for value in result
        ]

        return result


    async def __getitem__(self, key: str) -> ConfigValue:
        """
        Asynchronous get config value.

        Parameters
        ----------
        key : Config key.

        Returns
        -------
        Config value.
        """

        # Get.
        value = await self.get(key, Null)

        # Check.
        if value == Null:
            throw(KeyError, key)

        return value


    async def __setitem__(self, key_note: str | tuple[str, str], value: ConfigValue) -> None:
        """
        Asynchronous set config value.

        Parameters
        ----------
        key_note : Config key and note.
        value : Config value.
        """

        # Set parameter.
        if type(key_note) != str:
            key, note = key_note
        else:
            key = key_note
            note = None

        # Set.
        data = {
            'key': key,
            'value': repr(value),
            'type': type(value).__name__,
            'note': note
        }
        await self.db.execute.insert(
            self.db_names['config'],
            data,
            'update'
        )
