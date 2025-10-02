#!/usr/bin/env python3
# vim: fileencoding=utf-8 ts=4
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: © Copyright 2024, 2025 by Christian Dönges. All rights reserved.
# SPDXID: SPDXRef-hardwareregister-py
"""Description of hardware registers.

    A register has a name and an offset (which can be an address). It may also
    have an initial (reset) value.

    A register is made up of one or more fields. A field starts at a (low)
    first bit and ends as a last (high) bit. The bit range is inclusive.

    The bits in the field can be converted to several types:
        - boolean (one bit only)
        - enum
        - integer (unsigned)

    A register value holds the value of a register.
    The :py:class:`Register` describes a register and the fields it contains.
    The :py:class:`RegisterValue` holds a register value and references a
    :py:class:`Register`.

    Example use
    -----------

    .. code-block:: python

        wdt_ctrla = Register('WDT.CTRLA', 0x0100,
                             RegisterDescription( 8, [
                                 RegisterFieldInt('PERIOD', 0, 3),
                                 RegisterFieldInt('WINDOW', 4, 7)])
                             )
        wdt_status = Register('WDT.STATUS', 0x0101,
                              RegisterDescription(8, [
                                  RegisterFieldBool('SYNCBUSY', 0),
                                  RegisterFieldBool('LOCK', 7)]),
                              0)

        @enum.unique
        class VrefAC0RegSel(enum.IntEnum):
            """"""
            V0_55 = 0x00
            V1_1  = 0x01
            V2_5  = 0x02
            V4_4  = 0x04
            res1  = 0x05
            res2  = 0x06
            AVDD  = 0x07

        vref_ctrla = Register('VREF.CTRLA', 0x00A0,
                              RegisterDescription(8, [
                                  RegisterFieldEnum('AC0REFSEL', 0, 2, VrefAC0RegSel)]),
                              0)

        nvmctrl_addr = Register('NVMCTRL.ADDR', 0x1008,
                                RegisterDescription(16, [
                                    RegisterFieldInt('ADDR', 0, 15, RegisterField.Endian.Big),]),
                                0)
        nvmctrl_addr_value = RegisterValue(nvmctrl_addr, 0x1234)
        nvmctrl_addr_value = RegisterValue(nvmctrl_addr, 0x1234)
        print(f'nvmctrl_addr_value 0x{nvmctrl_addr_value.value:04x} is {nvmctrl_addr_value}')
        nvmctrl_addr_value.value = 0x5678
        print(f'nvmctrl_addr_value 0x{nvmctrl_addr_value.value:04x} is {nvmctrl_addr_value}')

    Output:

    .. code-block:: text

        nvmctrl_addr_value 0x1234 is ADDR:4660
        nvmctrl_addr_value 0x5678 is ADDR:22136

"""
# Postpone type hint evaluation until after the entire class has been parsed.
# This was to become standard in 3.10 but will probably never be.
# @see https://stackoverflow.com/a/33533514
# @see https://mail.python.org/archives/list/python-dev@python.org/thread/CLVXXPQ2T2LQ5MP2Y53VVQFCXYWQJHKZ/
from __future__ import annotations

from collections import OrderedDict
import enum
import sys
from typing import Any, Generator, Type, TypeVar


class RegisterField:
    """Describe a field in a register."""

    @enum.unique
    class Endian(enum.Enum):
        """Endianness of a register."""
        Unknown = '??'
        """The endianness is unknown."""
        Big = 'BE'
        """Values are stored with the most significant byte at the lowest
        address and the least significant byte at the highest address.

        Example ::
            0x12345678 is stored as 0x12 0x34 0x56 0x78.
        """
        Litte = 'LE'
        """Values are stored with the least significant byte at the lowest
        address and the most significant byte at the highest address.

        Example ::
            0x12345678 is stored as 0x78 0x56 0x34 0x12.
        """
        Middle = 'ME'
        """Values are stored as big endian words where each word is stored
        as litte endian.

        Example ::
            0x12345678 is stored as 0x34 0x12 0x78 0x56.
        """

    def __init__(self, name: str,
                 first_bit: int = 0,
                 last_bit: int = 31,
                 conversion: Type = None,
                 endian: Endian = Endian.Unknown):
        """Initialize the instance.

        :param name: The name of the field.
        :param first_bit: The first bit of the register belonging to the field (inclusive).
        :param last_bit: The last bit of the register belonging to the field (inclusive).
        :param TypeVar conversion: The conversion class.
        :param Endian endian: Endianness of the field. This is only relevant for
            fields spanning byte boundaries.
        :raise IndexError: last_bit is smaller than first_bit.
        """
        self._name = name
        if first_bit > last_bit:
            raise IndexError("first bit larger than last bit")
        self._first_bit = first_bit
        self._last_bit = last_bit
        self._conversion = conversion
        self._endian = endian

    def __str__(self) -> str:
        s = f'<{self.__class__.__name__}: {self._name} [{self._first_bit}'
        if self._first_bit == self._last_bit:
            s += '] '
        else:
            s += f':{self.last_bit}] '
        if self._conversion is not None:
            s += f'{self._conversion.__name__}'
        else:
            s += 'None'
        if self._last_bit - self._first_bit > 7:
            s += f' ({self._endian.value})'
        s += '>'
        return s

    @property
    def conversion(self) -> Type:
        """Return class used to convert the value."""
        return self._conversion

    @property
    def endian(self) -> RegisterField.Endian:
        """Endianness of the field."""
        return self._endian

    @property
    def first_bit(self) -> int:
        """First bit of the register containing the field."""
        return self._first_bit

    @property
    def last_bit(self) -> int:
        """Last bit of the register containing the field."""
        return self._last_bit

    @property
    def mask(self) -> int:
        """A mask leaving only bits contained in the field."""
        left = (1 << (self._last_bit + 1)) - 1
        right = (1 << self._first_bit) - 1
        return left & ~right

    @property
    def name(self) -> str:
        """Name of the field."""
        return self._name

    @property
    def type(self) -> Type:
        """Type of the field."""
        return self._conversion

    def convert(self, value: Any) -> Any:
        """Convert the given value to the type of the field."""
        return self._conversion(value)


class RegisterFieldBool(RegisterField):
    """A field in a register that is a single bit."""

    def __init__(self, name: str, bit: int):
        """Initialize the instance.

        :param str name: Name of the field.
        :param int bit: The bit in the register of the field.
        """
        super().__init__(name, bit, bit, bool)


class RegisterFieldInt(RegisterField):
    """A register field containing an integral value."""

    def __init__(self, name: str,
                 first_bit: int,
                 last_bit: int,
                 endian: RegisterField.Endian = RegisterField.Endian.Unknown):
        """Initialize the instance.

        :param str name: Name of the field.
        :param int first_bit: First bit of the register containing the field (inclusive).
        :param int last_bit: Last bit of the register containing the field (inclusive).
        :param RegisterField.Endian endian: Endianness of the field. This is only relevant for
            fields spanning byte boundaries.
        """
        super().__init__(name, first_bit, last_bit, int, endian)
        self._min_value = 0
        self._max_value = (1 << (last_bit + 1 - first_bit)) - 1

    @property
    def min_value(self) -> int:
        """Minimum allowed value in the field (inclusive)."""
        return self._min_value

    @property
    def max_value(self) -> int:
        """Maximum allowed value in the field (inclusive)."""
        return self._max_value


class RegisterFieldEnum(RegisterField):
    def __init__(self, name: str, first_bit: int, last_bit: int, conversion: Type[enum.IntEnum]|Type[enum.IntFlag]):
        """Initialize the instance.

        :param str name: Name of the field.
        :param int first_bit: First bit of the register containing the field (inclusive).
        :param int last_bit: Last bit of the register containing the field (inclusive).
        :param TypeVar conversion: The conversion class which must be an enum.
        """
        super().__init__(name, first_bit, last_bit, conversion)


class RegisterDescription:
    """Describes the layout and fields of a register."""

    def __init__(self, nr_bits: int, fields: list[RegisterField]):
        """Initialize self.

        :param int nr_bits: Number of bits in the register.
        :param list[RegisterField] fields: Fields of the register.
        :raise IndexError: An error was found in the fields.
        :raise KeyError: A field name was used multiple times.
        """
        self._nr_bits = nr_bits
        self._fields_by_name = OrderedDict([(f.name, f) for f in sorted(fields, key=lambda field: field.name)])
        self._fields_by_start = OrderedDict([(f.first_bit, f) for f in sorted(fields, key=lambda field: field.first_bit)])
        # Make sure fields are sorted by rising first_bit.
        self._fields = self._fields_by_start.values()
        if len(self._fields) != len(self._fields_by_name):
            raise KeyError('field name multiply defined')
        if len(self._fields) != len(self._fields_by_start):
            raise KeyError('field position multiply defined')
        self.check_field_consistency()

    def __str__(self) -> str:
        """Convert instance to a human-readable string.

            :rtype: str
        """
        s = f'<{self.__class__.__name__} nr_bits:{self._nr_bits}' +\
            f' fields:['
        first = True
        for first_bit in sorted(self._fields_by_start.keys()):
            field = self._fields_by_start[first_bit]
            if not first:
                s += f', {field}'
            else:
                s += f'{field}'
                first = False
        s += ']>'
        return s

    def check_field_consistency(self):
        """Check that the fields are consistently defined.

        :raise IndexError: An error was found in the fields.
        """
        nr_bits = 0
        bit_offset = -1
        for field in self._fields:
            if bit_offset >= field.first_bit:
                raise IndexError('bits multiply defined')
            nr_bits += field.last_bit - field.first_bit + 1
            if nr_bits > self._nr_bits:
                raise IndexError('too many bits')

    def field(self, name: str) -> RegisterField:
        """Return the field with the given name.

            :param str name: Name of the field.
            :raise KeyError: The given name is not a field.
        """
        return self._fields_by_name[name]

    def fields_by_start_bit(self) -> Generator[RegisterField, None, None]:
        """Yield all register fields in rising order of their start bit.

            :return: A register field per call.
            :rtype: RegisterField
        """
        for field in self._fields:
            yield field

    def fields_by_end_bit(self) -> Generator[RegisterField, None, None]:
        """Yield all register fields in falling order of their end bit.

            :return: A register field per call.
            :rtype: RegisterField
        """
        for field in reversed(self._fields):
            yield field

    def mask_keep_field(self, field: RegisterField) -> int:
        """Create a mask to remove all bits not belonging to the field.

           :param RegisterField field: The field to mask.
           :return: A mask leaving only the bits belonging to the field.
        """
        return field.mask

    def mask_remove_field(self, field: RegisterField) -> int:
        """Create a mask to remove all bits belonging to the field.

            :param RegisterField field: The field to mask.
            :return: A mask removing all bits belonging to the field.
        """
        return ~field.mask

    def value_of_field(self, field: RegisterField, value: int) -> Any:
        """Return the value of the field in the register."""
        v = (value & field.mask) >> field.first_bit
        return field.convert(v)


class Register:
    """A register at an offset with a name and description."""

    def __init__(self, name: str,
                 offset: int,
                 description: RegisterDescription,
                 initial: int = -1):
        """Initialize self.

        :param str name: Name of the register.
        :param int offset: Offset of the register.
        :param RegisterDescription description: Description of the register.
        :param int initial: Initial value of the register after reset.
            Use -1 for unknown initial value.
        """
        self._name = name
        self._offset = offset
        self._description = description
        self._initial = initial

    def __str__(self) -> str:
        """Convert instance to a human-readable string.

            :rtype: str
        """
        s = f'<{self.__class__.__name__}:{self._name}' + \
            f' offset:0x{self._offset:0x} {self._description}>'
        return s

    @property
    def name(self) -> str:
        """Return the register name."""
        return self._name

    @property
    def offset(self) -> int:
        """Offset of the register in memory."""
        return self._offset

    @property
    def description(self) -> RegisterDescription:
        """Description of the register."""
        return self._description

    @property
    def initial(self) -> int:
        """Initial value of the register after reset. -1 is unknown."""
        return self._initial


class RegisterValue:
    def __init__(self, register: Register,
                 value: int):
        self.register = register
        self.value = value

    def __str__(self) -> str:
        """Convert instance to a human-readable string."""
        s = ''
        for field in self.register.description.fields_by_start_bit():
            v = self.register.description.value_of_field(field, self.value)
            if isinstance(v, enum.Enum):
                v = v.name
            s += f'{field.name}:{v} '
        return s.rstrip()

    def __getattr__(self, name: str) -> bool|int|enum.IntEnum|enum.IntFlag:
        """Get the value of the named field in the register.

        :param str name: Name of the field.
        :rtype: bool|int|enum.IntEnum|enum.IntFlag
        :return: Value of the field in the register.
        :raise AttributeError: the field does not exist.
        """
        the_field = self.register.description.field(name)
        value = (self.value & the_field.mask) >> the_field.first_bit
        return the_field.convert(value)

    def set(self, name: str, value: bool|int|enum.IntEnum|enum.IntFlag):
        """Set the value of the named field in the register.

        :param str name: Name of the field.
        :param bool|int|enum.IntEnum|enum.IntFlag value: Value of the field in the register.
        :raise AttributeError: the field does not exist.
        """
        the_field = self.register.description.field(name)
        v = int(value) << the_field.first_bit
        self._value = (self.value & ~the_field.mask) | v


def example():
    """Module demonstration."""
    wdt_ctrla = Register('WDT CTRLA', 0x0100,
                         RegisterDescription( 8, [
                             RegisterFieldInt('PERIOD', 0, 3),
                             RegisterFieldInt('WINDOW', 4, 7)])
                         )
    print(f'wdt_ctrla contains integer fields: {wdt_ctrla}')
    wdt_status = Register('WDT STATUS', 0x0101,
                          RegisterDescription(8, [
                              RegisterFieldBool('SYNCBUSY', 0),
                              RegisterFieldBool('LOCK', 7)]),
                          0)
    print(f'wdt_status contains boolean fields: {wdt_status}')

    @enum.unique
    class VrefAC0RegSel(enum.IntEnum):
        """"""
        V0_55 = 0x00
        """0.55V"""
        V1_1  = 0x01
        """1.1V"""
        V2_5  = 0x02
        """2.5V"""
        V4_4  = 0x04
        """4.4V"""
        res1  = 0x05
        """Reserved"""
        res2  = 0x06
        """Reserved"""
        AVDD  = 0x07
        """AVDD"""

    vref_ctrla = Register('VREF CTRLA', 0x00A0,
                          RegisterDescription(8, [
                              RegisterFieldEnum('AC0REFSEL', 0, 2, VrefAC0RegSel)]),
                          0)
    print(f'vref_ctrla contains enum fields: {vref_ctrla}')

    @enum.unique
    class NvmectrlCtrlACmd(enum.IntEnum):
        NoCommand = 0x00
        """No command."""
        WP = 0x01
        """Write page buffer to memory (NVMCTRL.ADDR selects which memory)."""
        EP = 0x02
        """Erase page buffer (NVMCTRL.ADDR selects which memory)."""
        ERWP = 0x03
        """Erase and write page buffer (NVMCTRL.ADDR selects which memory)."""
        PBC = 0x04
        """Page buffer clear."""
        CHER = 0x05
        """Chip erase: erase Flash and EEPROM (unless EESAVE in FUSE.SYSCFG is '1')."""
        EEER = 0x06
        """EEPROM Erase."""
        WFU = 0x07
        """Write fuse (only accessible through UPDI)."""
    nvmctrl_ctrla = Register('NVMCTRL CTRLA', 0x1000,
                              RegisterDescription(8, [
                                  RegisterFieldEnum('CTRLA', 0, 2, NvmectrlCtrlACmd),
                              ]),
                             0)
    print(f'nvmctrl_ctrla: {nvmctrl_ctrla}')
    nvmctrl_ctrla_value = RegisterValue(nvmctrl_ctrla, 0x03)
    print(f'nvmctrl_ctrla_value 0x{nvmctrl_ctrla_value.value:02x} is {nvmctrl_ctrla_value}')
    nvmctrl_addr = Register('NVMCTRL ADDR', 0x1008,
                            RegisterDescription(16, [
                                RegisterFieldInt('ADDR', 0, 15, RegisterField.Endian.Big),]),
                            0)
    print(f'nvmctrl_addr: {nvmctrl_addr}')
    nvmctrl_addr_value = RegisterValue(nvmctrl_addr, 0x1234)
    print(f'nvmctrl_addr_value 0x{nvmctrl_addr_value.value:04x} is {nvmctrl_addr_value}')
    nvmctrl_addr_value.value = 0x5678
    print(f'nvmctrl_addr_value 0x{nvmctrl_addr_value.value:04x} is {nvmctrl_addr_value}')

    wdt_ctrla_value = RegisterValue(wdt_ctrla, 0x73)
    print(f'wdt_ctrla_value 0x{wdt_ctrla_value.value:02x} is {wdt_ctrla_value}')
    wdt_status_value = RegisterValue(wdt_status, 0x80)
    print(f'wdt_status_value 0x{wdt_status_value.value:02x} is {wdt_status_value}')
    vref_ctrla_value = RegisterValue(vref_ctrla, 0x02)
    print(f'vref_ctrla_value 0x{vref_ctrla_value.value:02x} is {vref_ctrla_value}')
    vref_ctrla_value.value = 0x07
    print(f'vref_ctrla_value 0x{vref_ctrla_value.value:02x} is {vref_ctrla_value}')


if __name__ == '__main__':
    if sys.version_info < (3, 10):
        print('FATAL ERROR: Python 3.10.x or later is required.')
        sys.exit(1)
    example()
