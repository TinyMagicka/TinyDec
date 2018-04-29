#-*- coding: utf-8 -*-

from ctypes import *

EI_NIDENT = 16

class Elf_e_ident(LittleEndianStructure):
    _doc_ = """elf file e_ident field"""
    _fields_ = [
        ("EI_MAG0",     c_byte),  #
        ("EI_MAG1",     c_byte),  #
        ("EI_MAG2",     c_byte),  #
        ("EI_MAG3",     c_byte),  #
        ("EI_CLASS",    c_byte),  # File class;    1: 32-bit objects,   2:64-bit objects
        ("EI_DATA",     c_byte),  # Data encoding; 1: little endian,    2: big endian
        ("EI_VERSION",  c_byte),  #
        ("EI_OSABI",    c_byte),  #
        ("EI_ABIVERSION", c_byte),  #
        ("EI_PAD",      c_byte*7)

    ]

class Elf32_Ehdr_LSB(LittleEndianStructure):
    _doc_ = """The ELF32 LittleEndian file header.  This appears at the start of every ELF file"""
    _fields_ = [
        ("e_ident",     Elf_e_ident),	# Magic number and other info
        ("e_type",      c_ushort),			# Object file type
        ("e_machine",   c_ushort),		# Architecture
        ("e_version",   c_uint),	    # Object file version
        ("e_entry",     c_uint),		# Entry point virtual address
        ("e_phoff",     c_uint),		# Program header table file offset
        ("e_shoff",     c_uint),		# Section header table file offset
        ("e_flags",     c_uint),		# Processor-specific flags
        ("e_ehsize",    c_ushort),		# ELF header size in bytes
        ("e_phentsize", c_ushort),		# Program header table entry size
        ("e_phnum",     c_ushort),		# Program header table entry count
        ("e_shentsize", c_ushort),		# Section header table entry size
        ("e_shnum",     c_ushort),		# Section header table entry count
        ("e_shstrndx",  c_ushort)		# Section header string table index
    ]

class Elf64_Ehdr_LSB(LittleEndianStructure):
    _doc_ = """The ELF64 LittleEndian file header.  This appears at the start of every ELF file"""
    _fields_ = [
        ("e_ident",     c_ubyte * EI_NIDENT),	# Magic number and other info
        ("e_type",      c_ushort),			# Object file type
        ("e_machine",   c_ushort),		# Architecture
        ("e_version",   c_uint),		# Object file version
        ("e_entry",     c_ulonglong),		# Entry point virtual address
        ("e_phoff",     c_ulonglong),		# Program header table file offset
        ("e_shoff",     c_ulonglong),		# Section header table file offset
        ("e_flags",     c_uint),		# Processor-specific flags
        ("e_ehsize",    c_ushort),		# ELF header size in bytes
        ("e_phentsize", c_ushort),		# Program header table entry size
        ("e_phnum",     c_ushort),		# Program header table entry count
        ("e_shentsize", c_ushort),		# Section header table entry size
        ("e_shnum",     c_ushort),		# Section header table entry count
        ("e_shstrndx",  c_ushort)		# Section header string table index
    ]

class Elf32_Shdr_LSB(LittleEndianStructure):
    _doc_ = "the ELF32 LittleEndian Section header"""
    _field = [
        ("sh_name",     c_uint), # Section name (string tbl index)
        ("sh_type",    	c_uint),	# Section type
        ("sh_flags",    c_uint),	# Section flags
        ("sh_addr",    	c_uint),# Section virtual addr at execution
        ("sh_offset",   c_uint),# Section file offset
        ("sh_size",     c_uint),# Section size in bytes
        ("sh_link",    	c_uint),# Link to another section
        ("sh_info",    	c_uint),# Additional section information
        ("sh_addralign",c_uint),	# Section alignment
        ("sh_entsize",  c_uint)# Entry size if section holds table
    ]

class Elf64_Shdr_LSB(LittleEndianStructure):
    _doc_ = "the ELF64 LittleEndian Section header"""
    _field = [
        ("sh_name",     c_uint), # Section name (string tbl index)
        ("sh_type",    	c_uint),	# Section type
        ("sh_flags",    c_ulonglong),	# Section flags
        ("sh_addr",    	c_ulonglong),# Section virtual addr at execution
        ("sh_offset",   c_ulonglong),# Section file offset
        ("sh_size",     c_ulonglong),# Section size in bytes
        ("sh_link",    	c_uint),# Link to another section
        ("sh_info",    	c_uint),# Additional section information
        ("sh_addralign",c_ulonglong),	# Section alignment
        ("sh_entsize",  c_ulonglong)# Entry size if section holds table
    ]

class Elf32_Phdr_LSB(LittleEndianStructure):
    _doc_ = """the ELF32 LittleEndian Program segment header"""
    _fields_ = [
        ("p_type",      c_uint), # Segment type
        ("p_offset",    c_uint), # Segment file offset
        ("p_vaddr",     c_uint), # Segment virtual address
        ("p_paddr",     c_uint), # Segment physical address
        ("p_filesz",    c_uint), # Segment size in file
        ("p_memsz",     c_uint), # Segment size in memory
        ("p_flags",     c_uint), # Segment flags
        ("p_align",     c_uint)  # Segment alignment
    ]

class Elf64_Phdr_LSB(LittleEndianStructure):
    _doc_ = """the ELF64 LittleEndian Program segment header"""
    _fields_ = [
        ("p_type",      c_uint), # Segment type
        ("p_flags",     c_uint), # Segment flags
        ("p_offset",    c_ulonglong), # Segment file offset
        ("p_vaddr",     c_ulonglong), # Segment virtual address
        ("p_paddr",     c_ulonglong), # Segment physical address
        ("p_filesz",    c_ulonglong), # Segment size in file
        ("p_memsz",     c_ulonglong), # Segment size in memory
        ("p_align",     c_ulonglong)  # Segment alignment
    ]


class Elf32_Ehdr_MSB(BigEndianStructure):
    _fields_ = [
        ("e_ident", c_ubyte * 16),
        ("e_type", c_ushort),
        ("e_machine", c_ushort),
        ("e_version", c_uint),
        ("e_entry", c_uint),
        ("e_phoff", c_uint),
        ("e_shoff", c_uint),
        ("e_flags", c_uint),
        ("e_ehsize", c_ushort),
        ("e_phentsize", c_ushort),
        ("e_phnum", c_ushort),
        ("e_shentsize", c_ushort),
        ("e_shnum", c_ushort),
        ("e_shstrndx", c_ushort)
    ]


class Elf64_Ehdr_MSB(BigEndianStructure):
    _fields_ = [
        ("e_ident", c_ubyte * 16),
        ("e_type", c_ushort),
        ("e_machine", c_ushort),
        ("e_version", c_uint),
        ("e_entry", c_ulonglong),
        ("e_phoff", c_ulonglong),
        ("e_shoff", c_ulonglong),
        ("e_flags", c_uint),
        ("e_ehsize", c_ushort),
        ("e_phentsize", c_ushort),
        ("e_phnum", c_ushort),
        ("e_shentsize", c_ushort),
        ("e_shnum", c_ushort),
        ("e_shstrndx", c_ushort)
    ]


class Elf32_Phdr_MSB(BigEndianStructure):
    _fields_ = [
        ("p_type", c_uint),
        ("p_offset", c_uint),
        ("p_vaddr", c_uint),
        ("p_paddr", c_uint),
        ("p_filesz", c_uint),
        ("p_memsz", c_uint),
        ("p_flags", c_uint),
        ("p_align", c_uint)
    ]


class Elf64_Phdr_MSB(BigEndianStructure):
    _fields_ = [
        ("p_type", c_uint),
        ("p_flags", c_uint),
        ("p_offset", c_ulonglong),
        ("p_vaddr", c_ulonglong),
        ("p_paddr", c_ulonglong),
        ("p_filesz", c_ulonglong),
        ("p_memsz", c_ulonglong),
        ("p_align", c_ulonglong)
    ]


class Elf32_Shdr_MSB(BigEndianStructure):
    _fields_ = [
        ("sh_name", c_uint),
        ("sh_type", c_uint),
        ("sh_flags", c_uint),
        ("sh_addr", c_uint),
        ("sh_offset", c_uint),
        ("sh_size", c_uint),
        ("sh_link", c_uint),
        ("sh_info", c_uint),
        ("sh_addralign", c_uint),
        ("sh_entsize", c_uint)
    ]


class Elf64_Shdr_MSB(BigEndianStructure):
    _fields_ = [
        ("sh_name", c_uint),
        ("sh_type", c_uint),
        ("sh_flags", c_ulonglong),
        ("sh_addr", c_ulonglong),
        ("sh_offset", c_ulonglong),
        ("sh_size", c_ulonglong),
        ("sh_link", c_uint),
        ("sh_info", c_uint),
        ("sh_addralign", c_ulonglong),
        ("sh_entsize", c_ulonglong)
    ]


class ELF:
    def __init__(self, binary):
        self.__binary = binary
        self.elfHeader = None
        self.sectionHeaderList = []
        self.programSegmentHeaderList = []
        self.setElfHeader()
        self.setSectionHeaderList()
        self.setProgramSegmentHeaderList()

    def setElfHeader(self):
        e_ident = Elf_e_ident.from_buffer_copy(self.__binary[:16])
        self.elfHeader = {
            (1, 1): Elf32_Ehdr_LSB,
            (1, 2): Elf32_Ehdr_MSB,
            (2, 1): Elf64_Ehdr_LSB,
            (2, 2): Elf64_Ehdr_MSB,
        }[(e_ident.EI_CLASS, e_ident.EI_DATA)].from_buffer_copy(self.__binary)

    def setSectionHeaderList(self):
        shdr_num = self.elfHeader.e_shnum
        base = self.__binary[self.elfHeader.e_shoff:]
        createShdr = {
                (1, 1): Elf32_Shdr_LSB,
                (1, 2): Elf32_Shdr_MSB,
                (2, 1): Elf64_Shdr_LSB,
                (2, 2): Elf64_Shdr_MSB,
            }[(self.elfHeader.e_ident.EI_CLASS, self.elfHeader.e_ident.EI_DATA)].from_buffer_copy
        for i in range(shdr_num):
            shdr = createShdr(base)
            self.sectionHeaderList.append(shdr)
            base = base[self.elfHeader.e_shentsize:]

    def setProgramSegmentHeaderList(self):
        phdr_num = self.elfHeader.e_phnum
        base = self.__binary[self.elfHeader.e_phoff:]
        createPhdr = {
                (1, 1): Elf32_Phdr_LSB,
                (1, 2): Elf32_Phdr_MSB,
                (2, 1): Elf64_Phdr_LSB,
                (2, 2): Elf64_Phdr_MSB,
            }[(self.elfHeader.e_ident.EI_CLASS, self.elfHeader.e_ident.EI_DATA)].from_buffer_copy
        for i in range(phdr_num):
            phdr = createPhdr(base)
            self.programSegmentHeaderList.append(phdr)
            base = base[self.elfHeader.e_phentsize:]

    def getType(self):
        type = {
            0: "ET_NONE",				# No file type
            1: "ET_REL",				# Relocatable file
            2: "ET_EXEC",				# Executable file
            3: "ET_DYN",			    # Shared object file
            4: "ET_CORE",				# Core file
            5: "ET_NUM",				# Number of defined types
            0xfe00: "ET_LOOS",			# OS-specific range start
            0xfeff: "ET_HIOS",			# OS-specific range end
            0xff00: "ET_LOPROC",		# Processor-specific range start
            0xffff: "ET_HIPROC"			# Processor-specific range end
        }
        return (self.elfHeader.e_type, type[self.elfHeader.e_type])

    def getEntry(self):
        return self.elfHeader.e_entry






if __name__ == "__main__":
    elf = ELF(open("../../test-suite-binaries/elf-ARMv7-ls", "r").read())
    print "entry is 0x%x" % elf.getEntry()
    print "type  is %s" % elf.getType()[1]
    print "\nSections =====================================:"
    num = 0
    for i in elf.sectionHeaderList:
        print num, i
        num +=1
