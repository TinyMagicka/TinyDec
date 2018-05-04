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
    _fields_ = [
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
    _fields_ = [
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

class ELF_Header():
    def __init__(self, header):
        self.elfHeader = header

    def __getattr__(self, attr):
        return self.elfHeader.__getattribute__(attr)

    def get_e_ident(self):
        s = "Magic (e_ident): \n"
        s += "\tMagic number 0 (EI_MAG0)                0x%2x\n" % (self.elfHeader.e_ident.EI_MAG0)
        s += "\tMagic number 1 (EI_MAG1)                %c\n" % (self.elfHeader.e_ident.EI_MAG1)
        s += "\tMagic number 2 (EI_MAG2)                %c\n" % (self.elfHeader.e_ident.EI_MAG2)
        s += "\tMagic number 3 (EI_MAG3)                %c\n" % (self.elfHeader.e_ident.EI_MAG3)
        t = {0: "WRONG!", 1: "32-bit", 2: "64-bit", 3: "WRONG!"}
        s += "\tFile class     (EI_CLASS)               0x%x: %-10s \n" % (self.elfHeader.e_ident.EI_CLASS, t[self.elfHeader.e_ident.EI_CLASS])
        t = {0: "WRONG!", 1: "2's complement, little endian", 2: "2's complement, big endian", 3: "WRONG!"}
        s += "\tData encoding  (EI_DATA)                0x%x: %-10s \n" % (self.elfHeader.e_ident.EI_DATA, t[self.elfHeader.e_ident.EI_DATA])
        s += "\tFile version   (EI_VERSION)             0x%x\n" % (self.elfHeader.e_ident.EI_VERSION)
        t = {
            0: "UNIX System V ABI",
            1: "HP-UX",
            2: "NetBSD",
            3: "Object uses GNU ELF extensions",
            6: "Sun Solaris",
            7: "IBM AIX",
            8: "SGI Irix",
            9: "FreeBSD",
            10: "Compaq TRU64 UNIX",
            11: "Novell Modesto",
            12: "OpenBSD",
            64: "ARM EABI",
            97: "ARM ",
            255: "Standalone (embedded) application",
        }
        s += "\tOS ABI         (EI_OSABI)               0x%x: %s\n" % (self.elfHeader.e_ident.EI_OSABI, t[self.elfHeader.e_ident.EI_OSABI])
        s += "\tABI version    (EI_ABIVERSION)          0x%x\n" % (self.elfHeader.e_ident.EI_ABIVERSION)
        s += "\tpadding bytes  (EI_PAD)                 0x%x%x%x%x%x%x%x\n" % tuple((i for i in self.elfHeader.e_ident.EI_PAD))
        return (self.elfHeader.e_ident, s)

        return self.elfHeader.e_ident

    def get_e_type(self):
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

    def get_e_machine(self):
        t = {
            0: "No machine",
            1: "AT&T WE 32100",
            2: "SUN SPARC",
            3: "Intel 80386",
            4: "Motorola m68k family",
            5: "Motorola m88k family",
            6: "Intel MCU",
            7: "Intel 80860",
            8: "MIPS R3000 big-endian",
            9: "IBM System/370",
            10: "MIPS R3000 little-endian",
            15: "HPPA",
            17: "Fujitsu VPP500",
            18: "Sun's \"v8plus\"",
            19: "Intel 80960",
            20: "PowerPC",
            21: "PowerPC 64-bit",
            22: "IBM S390",
            23: "IBM SPU/SPC",
            36: "NEC V800 series",
            37: "Fujitsu FR20",
            38: "TRW RH-32",
            39: "Motorola RCE",
            40: "ARM",
            41: "Digital Alpha",
            42: "Hitachi SH",
            43: "SPARC v9 64-bit",
            44: "Siemens Tricore",
            45: "Argonaut RISC Core",
            46: "Hitachi H8/300",
            47: "Hitachi H8/300H",
            48: "Hitachi H8S",
            49: "Hitachi H8/500",
            50: "Intel Merced",
            51: "Stanford MIPS-X",
            52: "Motorola Coldfire",
            53: "Motorola M68HC12",
            54: "Fujitsu MMA Multimedia Accelerator",
            55: "Siemens PCP",
            56: "Sony nCPU embeeded RISC",
            57: "Denso NDR1 microprocessor",
            58: "Motorola Start*Core processor",
            59: "Toyota ME16 processor",
            60: "STMicroelectronic ST100 processor",
            61: "Advanced Logic Corp. Tinyj emb.fam",
            62: "AMD x86-64 architecture",
            63: "Sony DSP Processor",
            64: "Digital PDP-10",
            65: "Digital PDP-11",
            66: "Siemens FX66 microcontroller",
            67: "STMicroelectronics ST9+ 8/16 mc",
            68: "STmicroelectronics ST7 8 bit mc",
            69: "Motorola MC68HC16 microcontroller",
            70: "Motorola MC68HC11 microcontroller",
            71: "Motorola MC68HC08 microcontroller",
            72: "Motorola MC68HC05 microcontroller",
            73: "Silicon Graphics SVx",
            74: "STMicroelectronics ST19 8 bit mc",
            75: "Digital VAX",
            76: "Axis Communications 32-bit emb.proc",
            77: "Infineon Technologies 32-bit emb.proc",
            78: "Element 14 64-bit DSP Processor",
            79: "LSI Logic 16-bit DSP Processor",
            80: "Donald Knuth's educational 64-bit proc",
            81: "Harvard University machine-independent object files",
            82: "SiTera Prism",
            83: "Atmel AVR 8-bit microcontroller",
            84: "Fujitsu FR30",
            85: "Mitsubishi D10V",
            86: "Mitsubishi D30V",
            87: "NEC v850",
            88: "Mitsubishi M32R",
            89: "Matsushita MN10300",
            90: "Matsushita MN10200",
            91: "picoJava",
            92: "OpenRISC 32-bit embedded processor",
            93: "ARC International ARCompact",
            94: "Tensilica Xtensa Architecture",
            95: "Alphamosaic VideoCore",
            96: "Thompson Multimedia General Purpose Proc",
            97: "National Semi. 32000",
            98: "Tenor Network TPC",
            99: "Trebia SNP 1000",
            100: "STMicroelectronics ST200",
            101: "Ubicom IP2xxx",
            102: "MAX processor",
            103: "National Semi. CompactRISC",
            104: "Fujitsu F2MC16",
            105: "Texas Instruments msp430",
            106: "Analog Devices Blackfin DSP",
            107: "Seiko Epson S1C33 family",
            108: "Sharp embedded microprocessor",
            109: "Arca RISC",
            110: "PKU-Unity & MPRC Peking Uni. mc series",
            111: "eXcess configurable cpu",
            112: "Icera Semi. Deep Execution Processor",
            113: "Altera Nios II",
            114: "National Semi. CompactRISC CRX",
            115: "Motorola XGATE",
            116: "Infineon C16x/XC16x",
            117: "Renesas M16C",
            118: "Microchip Technology dsPIC30F",
            119: "Freescale Communication Engine RISC",
            120: "Renesas M32C",
            131: "Altium TSK3000",
            132: "Freescale RS08",
            133: "Analog Devices SHARC family",
            134: "Cyan Technology eCOG2",
            135: "Sunplus S+core7 RISC",
            136: "New Japan Radio (NJR) 24-bit DSP",
            137: "Broadcom VideoCore III",
            138: "RISC for Lattice FPGA",
            139: "Seiko Epson C17",
            140: "Texas Instruments TMS320C6000 DSP",
            141: "Texas Instruments TMS320C2000 DSP",
            142: "Texas Instruments TMS320C55x DSP",
            143: "Texas Instruments App. Specific RISC",
            144: "Texas Instruments Prog. Realtime Unit",
            160: "STMicroelectronics 64bit VLIW DSP",
            161: "Cypress M8C",
            162: "Renesas R32C",
            163: "NXP Semi. TriMedia",
            164: "QUALCOMM DSP6",
            165: "Intel 8051 and variants",
            166: "STMicroelectronics STxP7x",
            167: "Andes Tech. compact code emb. RISC",
            168: "Cyan Technology eCOG1X",
            169: "Dallas Semi. MAXQ30 mc",
            170: "New Japan Radio (NJR) 16-bit DSP",
            171: "M2000 Reconfigurable RISC",
            172: "Cray NV2 vector architecture",
            173: "Renesas RX",
            174: "Imagination Tech. META",
            175: "MCST Elbrus",
            176: "Cyan Technology eCOG16",
            177: "National Semi. CompactRISC CR16",
            178: "Freescale Extended Time Processing Unit",
            179: "Infineon Tech. SLE9X",
            180: "Intel L10M",
            181: "Intel K10M",
            183: "ARM AARCH64",
            185: "Amtel 32-bit microprocessor",
            186: "STMicroelectronics STM8",
            187: "Tileta TILE64",
            188: "Tilera TILEPro",
            189: "Xilinx MicroBlaze",
            190: "NVIDIA CUDA",
            191: "Tilera TILE-Gx",
            192: "CloudShield",
            193: "KIPO-KAIST Core-A 1st gen.",
            194: "KIPO-KAIST Core-A 2nd gen.",
            195: "Synopsys ARCompact V2",
            196: "Open8 RISC",
            197: "Renesas RL78",
            198: "Broadcom VideoCore V",
            199: "Renesas 78KOR",
            200: "Freescale 56800EX DSC",
            201: "Beyond BA1",
            202: "Beyond BA2",
            203: "XMOS xCORE",
            204: "Microchip 8-bit PIC(r)",
            210: "KM211 KM32",
            211: "KM211 KMX32",
            212: "KM211 KMX16",
            213: "KM211 KMX8",
            214: "KM211 KVARC",
            215: "Paneve CDP",
            216: "Cognitive Smart Memory Processor",
            217: "Bluechip CoolEngine",
            218: "Nanoradio Optimized RISC",
            219: "CSR Kalimba",
            220: "Zilog Z80",
            221: "Controls and Data Services VISIUMcore",
            222: "FTDI Chip FT32",
            223: "Moxie processor",
            224: "AMD GPU",
            243: "RISC-V",
            247: "Linux BPF -- in-kernel virtual machine"
        }
        s = "%-35s %-20s %d: %s\n" % ("Architecture", "(e_machine)", self.elfHeader.e_machine, t[self.elfHeader.e_machine])
        return (self.elfHeader.e_machine, s)

    def get_e_version(self):
        s = "%-35s %-20s %d\n" % ("Version", "(e_version)", self.elfHeader.e_version)
        return (self.elfHeader.e_version, s)

    def get_e_entry(self):
        s = "%-35s %-20s 0x%x\n" % ("Entry Virtual Address", "(e_entry)", self.elfHeader.e_entry)
        return (self.elfHeader.e_entry, s)

    def get_e_phoff(self):
        s = "%-35s %-20s 0x%x\n" % ("Program header table file offset", "(e_phoff)", self.elfHeader.e_phoff)
        return (self.elfHeader.e_phoff, s)

    def get_e_shoff(self):
        s = "%-35s %-20s 0x%x\n" % ("Section header table file offset", "(e_shoff)", self.elfHeader.e_shoff)
        return (self.elfHeader.e_shoff, s)

    def get_e_flags(self):
        s = "%-35s %-20s 0x%x\n" % ("Processor-specific flags", "(e_flags)", self.elfHeader.e_flags)
        return (self.elfHeader.e_flags, s)

    def get_e_ehsize(self):
        s = "%-35s %-20s 0x%x\n" % ("ELF header size (bytes)", "(e_ehsize)", self.elfHeader.e_ehsize)
        return (self.elfHeader.e_ehsize, s)

    def get_e_phentsize(self):
        s = "%-35s %-20s 0x%x\n" % ("Program header table entry size", "(e_phentsize)", self.elfHeader.e_phentsize)
        return (self.elfHeader.e_phentsize, s)

    def get_e_phnum(self):
        s = "%-35s %-20s 0x%x(%d)\n" % ("Program header table entry count", "(e_phnum)", self.elfHeader.e_phnum, self.elfHeader.e_phnum)
        return (self.elfHeader.e_phnum, s)

    def get_e_shentsize(self):
        s = "%-35s %-20s 0x%x\n" % ("Section header table entry size", "(e_shentsize)", self.elfHeader.e_shentsize)
        return (self.elfHeader.e_shentsize, s)

    def get_e_shnum(self):
        s = "%-35s %-20s 0x%x(%d)\n" % ("Section header table entry count", "(e_shnum)", self.elfHeader.e_shnum, self.elfHeader.e_shnum)
        return (self.elfHeader.e_shnum, s)

    def get_e_shstrndx(self):
        s = "%-35s %-20s 0x%x(%d)\n" % ("Section header string table index", "(e_shstrndx)", self.elfHeader.e_shstrndx, self.elfHeader.e_shstrndx)
        return (self.elfHeader.e_shstrndx, s)

class ELF_Section_Header():
    def __init__(self, header):
        self.SectionHeader = header

    def __getattr__(self, item):
        return self.SectionHeader.__getattribute__(item)

    def getDescription(self):
        t = "0x%-10x"*10 + "\n"
        s = t % (self.sh_name, self.sh_type, self.sh_flags, self.sh_addr, self.sh_offset,\
             self.sh_size, self.sh_link, self.sh_info, self.sh_addralign, self.sh_entsize)
        return s



class ELF:
    def __init__(self, binary):
        self.__binary = binary
        self.elfHeader = None
        self.sectionHeaderList = []
        self.programSegmentHeaderList = []
        self.__setElfHeader()
        self.__setSectionHeaderList()
        self.__setProgramSegmentHeaderList()
        self.__setSectionHeaderStrings()

    def __setElfHeader(self):
        e_ident = Elf_e_ident.from_buffer_copy(self.__binary[:16])
        elfHeader = {
            (1, 1): Elf32_Ehdr_LSB,
            (1, 2): Elf32_Ehdr_MSB,
            (2, 1): Elf64_Ehdr_LSB,
            (2, 2): Elf64_Ehdr_MSB,
        }[(e_ident.EI_CLASS, e_ident.EI_DATA)].from_buffer_copy(self.__binary)
        self.elfHeader = ELF_Header(elfHeader)

    def __setSectionHeaderList(self):
        shdr_num = self.elfHeader.e_shnum
        base = self.__binary[self.elfHeader.e_shoff:]
        createShdr = {
                (1, 1): Elf32_Shdr_LSB,
                (1, 2): Elf32_Shdr_MSB,
                (2, 1): Elf64_Shdr_LSB,
                (2, 2): Elf64_Shdr_MSB,
            }[(self.elfHeader.e_ident.EI_CLASS, self.elfHeader.e_ident.EI_DATA)].from_buffer_copy
        for i in range(shdr_num):
            shdr = ELF_Section_Header(createShdr(base))
            self.sectionHeaderList.append(shdr)
            base = base[self.elfHeader.e_shentsize:]

    def __setProgramSegmentHeaderList(self):
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

    def __setSectionHeaderStrings(self):
        shstrndx = self.elfHeader.e_shstrndx
        shstrtableSection = self.sectionHeaderList[shstrndx]
        base = self.__binary[shstrtableSection.sh_offset:shstrtableSection.sh_offset+shstrtableSection.sh_size]
        for s in self.sectionHeaderList:
            i = s.sh_name
            j = i
            while base[j] != "\x00" and j<len(base): j += 1
            if j<len(base):
                tmp = str(base[i:j])
                s.sh_name_str = tmp

        self.SectionHeaderStringTable = s

    def getHeadDescription(self):
        s = "=================================Head main description=================================\n"
        s += self.elfHeader.get_e_ident()[1]
        s += self.elfHeader.get_e_machine()[1]
        s += self.elfHeader.get_e_version()[1]
        s += self.elfHeader.get_e_entry()[1]
        s += self.elfHeader.get_e_phoff()[1]
        s += self.elfHeader.get_e_shoff()[1]
        s += self.elfHeader.get_e_flags()[1]
        s += self.elfHeader.get_e_ehsize()[1]
        s += self.elfHeader.get_e_phentsize()[1]
        s += self.elfHeader.get_e_phnum()[1]
        s += self.elfHeader.get_e_shentsize()[1]
        s += self.elfHeader.get_e_shnum()[1]
        s += self.elfHeader.get_e_shstrndx()[1]
        return s

    def getSectionHeaderListDesctiption(self):
        s = "=================================Section Header List description=================================\n"
        t = "        %-25s" + "%-12s"*9 + "\n"
        s += t % ("name_str", "type", "flags", "v_addr", "offset", "size", "link", "info", "addralign", "entsize")
        num = 0
        for i in self.sectionHeaderList:
            t = "[%4d]  %-25s" + "0x%-10x" * 9 + "\n"
            s += t % (num, i.sh_name_str, i.sh_type, i.sh_flags, i.sh_addr, i.sh_offset, \
                     i.sh_size, i.sh_link, i.sh_info, i.sh_addralign, i.sh_entsize)
            num +=1
        return s




if __name__ == "__main__":
    elf = ELF(open("../../test-suite-binaries/elf-ARMv7-ls", "r").read())
    print elf.getHeadDescription()
    print elf.getSectionHeaderListDesctiption()
    num = 0
    for i in elf.SectionHeaderStringTable:
        print num, i
        num +=1
