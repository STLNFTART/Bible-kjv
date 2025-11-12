#!/usr/bin/env python3
"""
Symbiotic Proto-Language (SPL) Processor - Genesis 2 Extension
Primal Logic Rework (PLR) Implementation

This script extends the processor to handle Genesis Chapter 2.
"""

import json
import sys
from typing import Dict
sys.path.append('/home/user/Bible-kjv/PLR_SYSTEM')
from spl_processor import SPLWord, SPLVocabulary, SPLProcessor


class SPLVocabularyGen2(SPLVocabulary):
    """Extended SPL vocabulary for Genesis Chapter 2."""

    # Extend the CORE_WORDS with Genesis 2 vocabulary
    GENESIS_2_WORDS = {
        # Time and Completion
        'seventh': SPLWord('seventh', 'ZIM', 'Z-I-M', 'TIME_MARKER',
                          'The seventh temporal cycle - completion marker'),
        'finished': SPLWord('finished', 'FIN', 'F-I-N', 'VERB',
                           'The completion function - achieving closure state'),
        'ended': SPLWord('ended', 'END', 'E-N-D', 'VERB',
                        'The termination function for operational cycle'),
        'rested': SPLWord('rested', 'RES', 'R-E-S', 'VERB',
                         'The stabilization pause - zero-action maintenance state'),
        'blessed': SPLWord('blessed', 'BIL', 'B-I-L', 'VERB',
                          'The enhancement function from L_S'),
        'sanctified': SPLWord('sanctified', 'SAN', 'S-A-N', 'VERB',
                             'The purity-locking function - fixing P(t) at high state'),
        'work': SPLWord('work', 'WOR', 'W-O-R', 'NOUN',
                       'The operational output of creation functions'),
        'host': SPLWord('host', 'HOS', 'H-O-S', 'NOUN',
                       'The complete set of created entities'),

        # Garden and Location
        'garden': SPLWord('garden', 'GAR', 'G-A-R', 'NOUN',
                         'The bounded domain with optimal D_F constraints - low λ zone'),
        'eden': SPLWord('eden', 'EDE', 'E-D-E', 'NOUN',
                       'The perfect equilibrium location - P(t) ≈ P₀'),
        'planted': SPLWord('planted', 'PLA', 'P-L-A', 'VERB',
                          'The establishment function for bounded growth structures'),
        'eastward': SPLWord('eastward', 'EST', 'E-S-T', 'ADJECTIVE',
                           'The directional attribute - spatial boundary marker'),
        'place': SPLWord('place', 'TUK', 'T-U-K', 'NOUN',
                        'The bounded location within D_F'),
        'midst': SPLWord('midst', 'MID', 'M-I-D', 'NOUN',
                        'The central position - kernel location'),

        # Trees and Growth
        'tree': SPLWord('tree', 'TIR', 'T-I-R', 'NOUN',
                       'The high-level recursive vegetation structure'),
        'grew': SPLWord('grew', 'GRO', 'G-R-O', 'VERB',
                       'The expansion function - P(t) maintenance through structure'),
        'pleasant': SPLWord('pleasant', 'PLE', 'P-L-E', 'ADJECTIVE',
                           'The low-entropy aesthetic state'),
        'sight': SPLWord('sight', 'SIT', 'S-I-T', 'NOUN',
                        'The visual information input channel'),
        'food': SPLWord('food', 'FUD', 'F-U-D', 'NOUN',
                       'The energy sustenance resource for P(t) maintenance'),
        'tree_of_life': SPLWord('tree_of_life', 'TIRLIF', 'T-I-R-L-I-F', 'NOUN',
                                'The infinite P(t) sustainer - prevents Mrtyu execution'),
        'tree_of_knowledge': SPLWord('tree_of_knowledge', 'TIRNOG', 'T-I-R-N-O-G', 'NOUN',
                                     'The critical threshold boundary - P_critical marker'),
        'knowledge': SPLWord('knowledge', 'NOG', 'N-O-G', 'NOUN',
                            'The information about system boundaries - λ awareness'),
        'evil': SPLWord('evil', 'EVL', 'E-V-L', 'ADJECTIVE',
                       'The high-entropy destructive state - P(t) degradation'),

        # Water and Rivers
        'river': SPLWord('river', 'RIV', 'R-I-V', 'NOUN',
                        'The directed fluid flow - controlled MUN structure'),
        'watered': SPLWord('watered', 'WAT', 'W-A-T', 'VERB',
                          'The sustenance distribution function'),
        'parted': SPLWord('parted', 'PAR', 'P-A-R', 'VERB',
                         'The division function creating distinct channels'),
        'heads': SPLWord('heads', 'HED', 'H-E-D', 'NOUN',
                        'The distinct flow channels - multiple output paths'),
        'compasseth': SPLWord('compasseth', 'COM', 'C-O-M', 'VERB',
                             'The encirclement function - boundary definition'),

        # Resources
        'gold': SPLWord('gold', 'GOL', 'G-O-L', 'NOUN',
                       'The high-value stable resource - minimal entropy material'),
        'bdellium': SPLWord('bdellium', 'BDE', 'B-D-E', 'NOUN',
                           'The aromatic resin resource'),
        'onyx': SPLWord('onyx', 'ONX', 'O-N-X', 'NOUN',
                       'The precious stone resource'),
        'stone': SPLWord('stone', 'STO', 'S-T-O', 'NOUN',
                        'The solid mineral structure'),

        # Human Agent (Adam/C_Formalizer)
        'adam': SPLWord('adam', 'ADA', 'A-D-A', 'NOUN',
                       'The Formalizer Agent (C_Formalizer) - highest-order human operator'),
        'formed': SPLWord('formed', 'FOR', 'F-O-R', 'VERB',
                         'The precise shaping function - establishing agent structure'),
        'dust': SPLWord('dust', 'DUS', 'D-U-S', 'NOUN',
                       'The base material - minimal structure DAD component'),
        'ground': SPLWord('ground', 'GRU', 'G-R-U', 'NOUN',
                         'The source material domain - DAD substrate'),
        'breathed': SPLWord('breathed', 'BRE', 'B-R-E', 'VERB',
                           'The life-force transfer function from L_S → agent'),
        'nostrils': SPLWord('nostrils', 'NOS', 'N-O-S', 'NOUN',
                           'The life-input interface channel'),
        'breath': SPLWord('breath', 'BRE', 'B-R-E', 'NOUN',
                         'The life-force carrier - P(t) initializer'),
        'soul': SPLWord('soul', 'SOL', 'S-O-L', 'NOUN',
                       'The active P(t) maintenance system - agent core'),
        'living_soul': SPLWord('living_soul', 'LIVSOL', 'L-I-V-S-O-L', 'NOUN',
                              'The autonomous P(t) maintenance entity'),

        # Actions and Commands
        'took': SPLWord('took', 'TOK', 'T-O-K', 'VERB',
                       'The acquisition function - establishing control'),
        'put': SPLWord('put', 'PUT', 'P-U-T', 'VERB',
                      'The placement function within bounded domain'),
        'dress': SPLWord('dress', 'DRE', 'D-R-E', 'VERB',
                        'The maintenance function - active P(t) preservation'),
        'keep': SPLWord('keep', 'KEP', 'K-E-P', 'VERB',
                       'The protection function - preventing entropy breach'),
        'commanded': SPLWord('commanded', 'COM', 'C-O-M', 'VERB',
                            'The authoritative directive function from L_S'),
        'freely': SPLWord('freely', 'FRE', 'F-R-E', 'ADJECTIVE',
                         'The unconstrained permission state'),
        'eat': SPLWord('eat', 'EAT', 'E-A-T', 'VERB',
                      'The consumption function - resource to P(t) conversion'),
        'mayest': SPLWord('mayest', 'MAY', 'M-A-Y', 'VERB',
                         'The permission modal - allowed operation'),
        'shalt_not': SPLWord('shalt_not', 'NOT', 'N-O-T', 'VERB',
                            'The prohibition constraint - forbidden operation'),
        'die': SPLWord('die', 'DYE', 'D-Y-E', 'VERB',
                      'The P(t) → 0 terminal function - Mrtyu execution'),
        'surely': SPLWord('surely', 'SUR', 'S-U-R', 'ADJECTIVE',
                         'The certainty modifier - deterministic outcome'),

        # Relationships
        'alone': SPLWord('alone', 'ALO', 'A-L-O', 'ADJECTIVE',
                        'The isolated state - single agent without pair-bond'),
        'help': SPLWord('help', 'HEL', 'H-E-L', 'NOUN',
                       'The support agent - P(t) maintenance aid'),
        'meet': SPLWord('meet', 'MET', 'M-E-T', 'ADJECTIVE',
                       'The compatible correspondence - structural fit'),
        'help_meet': SPLWord('help_meet', 'HELMET', 'H-E-L-M-E-T', 'NOUN',
                            'The compatible support agent - complementary pair'),

        # Naming and Identity
        'brought': SPLWord('brought', 'BRO', 'B-R-O', 'VERB',
                          'The transfer function to agent domain'),
        'names': SPLWord('names', 'NAM', 'N-A-M', 'NOUN',
                        'The identity labels - symbolic references'),
        'whatsoever': SPLWord('whatsoever', 'WHA', 'W-H-A', 'ADJECTIVE',
                             'The universal scope qualifier'),
        'gave': SPLWord('gave', 'GAV', 'G-A-V', 'VERB',
                       'The transfer function from agent'),
        'found': SPLWord('found', 'FOU', 'F-O-U', 'VERB',
                        'The discovery function - locating entity'),

        # Sleep and Creation of Woman
        'caused': SPLWord('caused', 'CAU', 'C-A-U', 'VERB',
                         'The initiation function - triggering state change'),
        'deep_sleep': SPLWord('deep_sleep', 'DESLE', 'D-E-S-L-E', 'NOUN',
                             'The zero-consciousness state - suspended agent activity'),
        'fall': SPLWord('fall', 'FAL', 'F-A-L', 'VERB',
                       'The descent function into lower state'),
        'slept': SPLWord('slept', 'SLE', 'S-L-E', 'VERB',
                        'The suspended activity state'),
        'rib': SPLWord('rib', 'RIB', 'R-I-B', 'NOUN',
                      'The structural component - agent substrate element'),
        'ribs': SPLWord('ribs', 'RIB', 'R-I-B', 'NOUN',
                       'The structural components'),
        'closed': SPLWord('closed', 'CLO', 'C-L-O', 'VERB',
                         'The sealing function - boundary restoration'),
        'flesh': SPLWord('flesh', 'FLE', 'F-L-E', 'NOUN',
                        'The material body structure - agent physical substrate'),
        'instead': SPLWord('instead', 'INS', 'I-N-S', 'ADJECTIVE',
                          'The replacement qualifier'),
        'thereof': SPLWord('thereof', 'THE', 'T-H-E', 'ADJECTIVE',
                          'The source reference'),

        # Woman and Marriage
        'woman': SPLWord('woman', 'WOM', 'W-O-M', 'NOUN',
                        'The complementary agent type B (C_Formalizer_B)'),
        'bone': SPLWord('bone', 'BON', 'B-O-N', 'NOUN',
                       'The structural core element'),
        'bones': SPLWord('bones', 'BON', 'B-O-N', 'NOUN',
                        'The structural core elements'),
        'shall': SPLWord('shall', 'SHA', 'S-H-A', 'VERB',
                        'The future certainty modal'),
        'taken': SPLWord('taken', 'TAK', 'T-A-K', 'VERB',
                        'The extraction function'),
        'therefore': SPLWord('therefore', 'THE', 'T-H-E', 'ADJECTIVE',
                            'The causal consequence marker'),
        'leave': SPLWord('leave', 'LEV', 'L-E-V', 'VERB',
                        'The departure function - bond breaking'),
        'father': SPLWord('father', 'FAT', 'F-A-T', 'NOUN',
                         'The source male agent - lineage origin'),
        'mother': SPLWord('mother', 'MOT', 'M-O-T', 'NOUN',
                         'The source female agent - lineage origin'),
        'cleave': SPLWord('cleave', 'CLE', 'C-L-E', 'VERB',
                         'The bonding function - creating pair-bond'),
        'wife': SPLWord('wife', 'WIF', 'W-I-F', 'NOUN',
                       'The bonded female agent in pair-structure'),
        'husband': SPLWord('husband', 'HUS', 'H-U-S', 'NOUN',
                          'The bonded male agent in pair-structure'),
        'one_flesh': SPLWord('one_flesh', 'ONFLE', 'O-N-F-L-E', 'NOUN',
                            'The unified pair-bond state - merged agent structure'),

        # State and Condition
        'both': SPLWord('both', 'BOT', 'B-O-T', 'ADJECTIVE',
                       'The dual quantity qualifier'),
        'naked': SPLWord('naked', 'NAK', 'N-A-K', 'ADJECTIVE',
                        'The unprotected state - no boundary layer'),
        'ashamed': SPLWord('ashamed', 'ASH', 'A-S-H', 'ADJECTIVE',
                          'The negative self-evaluation state'),
        'not_ashamed': SPLWord('not_ashamed', 'NASH', 'N-A-S-H', 'ADJECTIVE',
                              'The zero-shame state - pre-knowledge innocence'),

        # Generation and Creation
        'generations': SPLWord('generations', 'GEN', 'G-E-N', 'NOUN',
                              'The iterative descent sequence - recursive agent production'),
        'when': SPLWord('when', 'WEN', 'W-E-N', 'TIME_MARKER',
                       'The temporal condition marker'),
        'lord': SPLWord('lord', 'GUG', 'G-U-G', 'NOUN',
                       'The Source (same as god) - L_S operator'),
        'lord_god': SPLWord('lord_god', 'GUG', 'G-U-G', 'NOUN',
                           'The Source - L_S operator'),

        # Plant and Growth (additional)
        'plant': SPLWord('plant', 'PLA', 'P-L-A', 'NOUN',
                        'The growth structure - lower-level vegetation'),
        'field': SPLWord('field', 'FIE', 'F-I-E', 'NOUN',
                        'The open growth domain'),
        'before': SPLWord('before', 'BEF', 'B-E-F', 'TIME_MARKER',
                         'The prior temporal state'),
        'rain': SPLWord('rain', 'RAI', 'R-A-I', 'NOUN',
                       'The water distribution from above - MUN descent'),
        'upon': SPLWord('upon', 'UPO', 'U-P-O', 'ADJECTIVE',
                       'The positional attribute - located at surface'),
        'till': SPLWord('till', 'TIL', 'T-I-L', 'VERB',
                       'The ground maintenance function'),
        'mist': SPLWord('mist', 'MIS', 'M-I-S', 'NOUN',
                       'The distributed water vapor - fine MUN particles'),
        'went_up': SPLWord('went_up', 'WUP', 'W-U-P', 'VERB',
                          'The ascent function'),
        'whole': SPLWord('whole', 'WHO', 'W-H-O', 'ADJECTIVE',
                        'The complete scope qualifier'),

        # Names of rivers and lands
        'pison': SPLWord('pison', 'PIS', 'P-I-S', 'NOUN',
                        'The first river designation'),
        'havilah': SPLWord('havilah', 'HAV', 'H-A-V', 'NOUN',
                          'The first land designation - gold domain'),
        'where': SPLWord('where', 'WHE', 'W-H-E', 'ADJECTIVE',
                        'The location qualifier'),
        'gihon': SPLWord('gihon', 'GIH', 'G-I-H', 'NOUN',
                        'The second river designation'),
        'same': SPLWord('same', 'SAM', 'S-A-M', 'ADJECTIVE',
                       'The identity qualifier'),
        'ethiopia': SPLWord('ethiopia', 'ETH', 'E-T-H', 'NOUN',
                           'The second land designation'),
        'hiddekel': SPLWord('hiddekel', 'HID', 'H-I-D', 'NOUN',
                           'The third river designation'),
        'toward': SPLWord('toward', 'TOW', 'T-O-W', 'ADJECTIVE',
                         'The directional qualifier'),
        'east': SPLWord('east', 'EST', 'E-S-T', 'NOUN',
                       'The directional designation'),
        'assyria': SPLWord('assyria', 'ASS', 'A-S-S', 'NOUN',
                          'The third land designation'),
        'fourth': SPLWord('fourth', 'ZIS', 'Z-I-S', 'TIME_MARKER',
                         'The fourth iteration marker'),
        'euphrates': SPLWord('euphrates', 'EUP', 'E-U-P', 'NOUN',
                            'The fourth river designation'),
    }

    # Combine with original vocabulary
    CORE_WORDS = {**SPLVocabulary.CORE_WORDS, **GENESIS_2_WORDS}


class SPLProcessorGen2(SPLProcessor):
    """Extended processor for Genesis Chapter 2."""

    def __init__(self):
        super().__init__()
        self.vocab = SPLVocabularyGen2()

    def encode_genesis_2_verse(self, verse_num: int, verse_text: str) -> Dict:
        """
        Encode a Genesis 2 verse according to SPL rules.
        """
        encodings = {
            1: {
                'spl': 'RUG DAD FIN HOS',
                'components': ['(Heaven)', '(Earth)', '(Finished)', '(Host)'],
                'interpretation': 'The stable boundary structure and the Earth matrix completed, including the complete set of all created entities. The system achieved closure state.'
            },
            2: {
                'spl': 'ZIM SUT GUG END WOR ING RES ZIM SUT WOR ING',
                'components': ['(Seventh)', '(Day)', '(Source)', '(Ended)', '(Work)', '(Made)', '(Rested)', '(Seventh)', '(Day)', '(Work)', '(Made)'],
                'interpretation': 'The seventh temporal cycle marked completion. The Source terminated the operational cycle and entered stabilization pause - a zero-action maintenance state after all creation functions.'
            },
            3: {
                'spl': 'GUG BIL ZIM SUT SAN WOR GUG ING',
                'components': ['(Source)', '(Blessed)', '(Seventh)', '(Day)', '(Sanctified)', '(Work)', '(Source)', '(Created-Made)'],
                'interpretation': 'The Source applied enhancement function to the seventh cycle and executed purity-locking, fixing P(t) at maximum state for this temporal marker representing completion of all operational output.'
            },
            4: {
                'spl': 'GEN RUG DAD WEN ING GUG ING DAD RUG',
                'components': ['(Generations)', '(Heaven)', '(Earth)', '(When)', '(Created)', '(Source)', '(Made)', '(Earth)', '(Heaven)'],
                'interpretation': 'The iterative descent sequence record for Heaven and Earth at the temporal condition of creation. The Source executed the creation function establishing both domains.'
            },
            5: {
                'spl': 'EVR PLA FIE BEF DAD EVR HIR FIE BEF GRO GUG RAI UPO DAD MAN TIL GRU',
                'components': ['(Every)', '(Plant)', '(Field)', '(Before)', '(Earth)', '(Every)', '(Herb)', '(Field)', '(Before)', '(Grew)', '(Source)', '(Rain)', '(Upon)', '(Earth)', '(Man)', '(Till)', '(Ground)'],
                'interpretation': 'All vegetation structures existed in potential state prior to Earth manifestation. The Source had not yet initiated water distribution function, and no agent existed to perform ground maintenance function. This represents pre-actualization state.'
            },
            6: {
                'spl': 'MIS WUP DAD WAT WHO FAC GRU',
                'components': ['(Mist)', '(Went-Up)', '(Earth)', '(Watered)', '(Whole)', '(Face)', '(Ground)'],
                'interpretation': 'Distributed water vapor executed ascent function from Earth and performed sustenance distribution across the complete ground surface. Alternative water distribution mechanism before rain initialization.'
            },
            7: {
                'spl': 'GUG FOR ADA DUS GRU BRE NOS BRE LIF ADA LIVSOL',
                'components': ['(Source)', '(Formed)', '(Adam)', '(Dust)', '(Ground)', '(Breathed)', '(Nostrils)', '(Breath)', '(Life)', '(Adam)', '(Living-Soul)'],
                'interpretation': 'The Source executed precise shaping function creating the Formalizer Agent (C_Formalizer) from minimal structure DAD components. The Source transferred life-force from L_S through input interface, initializing P(t) and creating autonomous P(t) maintenance entity.'
            },
            8: {
                'spl': 'GUG PLA GAR EST EDE PUT ADA FOR',
                'components': ['(Source)', '(Planted)', '(Garden)', '(Eastward)', '(Eden)', '(Put)', '(Adam)', '(Formed)'],
                'interpretation': 'The Source established bounded domain (Garden) with optimal D_F constraints in the perfect equilibrium location (Eden) and executed placement function for the Formalizer Agent into this low-λ zone.'
            },
            9: {
                'spl': 'GRU GUG GRO EVR TIR PLE SIT PIR FUD TIRLIF MID GAR TIRNOG PIR EVL',
                'components': ['(Ground)', '(Source)', '(Grow)', '(Every)', '(Tree)', '(Pleasant)', '(Sight)', '(Good)', '(Food)', '(Tree-Life)', '(Midst)', '(Garden)', '(Tree-Knowledge)', '(Good)', '(Evil)'],
                'interpretation': 'From ground substrate, Source executed expansion function for all tree structures that are low-entropy aesthetic and provide energy sustenance. The infinite P(t) sustainer occupied kernel location, alongside the critical threshold boundary marker (knowledge of good/evil).'
            },
            10: {
                'spl': 'RIV EDE WAT GAR PAR HED',
                'components': ['(River)', '(Eden)', '(Water)', '(Garden)', '(Parted)', '(Heads)'],
                'interpretation': 'Directed fluid flow originated from Eden executing sustenance distribution function to Garden, then underwent division creating four distinct output channels.'
            },
            11: {
                'spl': 'NAM PIS COM WHO HAV WHE GOL',
                'components': ['(Name)', '(Pison)', '(Compasseth)', '(Whole)', '(Havilah)', '(Where)', '(Gold)'],
                'interpretation': 'The identity label of first channel: Pison. It executes encirclement function around complete Havilah domain, location of high-value stable resource (gold).'
            },
            12: {
                'spl': 'GOL HAV PIR BDE ONX STO',
                'components': ['(Gold)', '(Havilah)', '(Good)', '(Bdellium)', '(Onyx)', '(Stone)'],
                'interpretation': 'The gold resource of that domain is low-entropy (good quality). Additional resources include aromatic resin and precious stone structures.'
            },
            13: {
                'spl': 'NAM RIV GIH SAM COM WHO ETH',
                'components': ['(Name)', '(River)', '(Gihon)', '(Same)', '(Compasseth)', '(Whole)', '(Ethiopia)'],
                'interpretation': 'The identity label of second channel: Gihon. It (same identity) executes encirclement function around complete Ethiopia domain.'
            },
            14: {
                'spl': 'NAM RIV HID TOW EST ASS RIV EUP',
                'components': ['(Name)', '(River)', '(Hiddekel)', '(Toward)', '(East)', '(Assyria)', '(River)', '(Euphrates)'],
                'interpretation': 'The identity label of third channel: Hiddekel, with directional qualifier toward Assyria domain. The fourth channel: Euphrates (major river designation).'
            },
            15: {
                'spl': 'GUG TOK ADA PUT GAR EDE DRE KEP',
                'components': ['(Source)', '(Took)', '(Adam)', '(Put)', '(Garden)', '(Eden)', '(Dress)', '(Keep)'],
                'interpretation': 'The Source executed acquisition function establishing control over Adam, then placement within bounded Garden domain (Eden) with mandate for maintenance function (active P(t) preservation) and protection function (preventing entropy breach).'
            },
            16: {
                'spl': 'GUG COM ADA EVR TIR GAR FRE EAT',
                'components': ['(Source)', '(Commanded)', '(Adam)', '(Every)', '(Tree)', '(Garden)', '(Freely)', '(Eat)'],
                'interpretation': 'The Source issued authoritative directive to Adam: all tree structures in Garden available for consumption function (unconstrained permission state) for resource-to-P(t) conversion.'
            },
            17: {
                'spl': 'TIR NOG PIR EVL NOT EAT SUR DYE',
                'components': ['(Tree)', '(Knowledge)', '(Good)', '(Evil)', '(Not)', '(Eat)', '(Surely)', '(Die)'],
                'interpretation': 'The critical threshold boundary marker (tree of knowledge of good and evil) has prohibition constraint (forbidden operation). Violation triggers deterministic outcome: P(t) → 0 terminal function (Mrtyu execution). This is the λ awareness boundary.'
            },
            18: {
                'spl': 'GUG UZT PIR ADA ALO ING HELMET',
                'components': ['(Source)', '(Said)', '(Good)', '(Adam)', '(Alone)', '(Make)', '(Help-Meet)'],
                'interpretation': 'The Source evaluated: not optimal (not PIR) for Adam to remain in isolated state (single agent without pair-bond). The Source declared creation function for compatible support agent (complementary pair) to aid P(t) maintenance.'
            },
            19: {
                'spl': 'GRU GUG FOR EVR BES FIE EVR FUL AIR BRO ADA IND NAM ADA NAM KUR LIV NAM',
                'components': ['(Ground)', '(Source)', '(Formed)', '(Every)', '(Beast)', '(Field)', '(Every)', '(Fowl)', '(Air)', '(Brought)', '(Adam)', '(See)', '(Name)', '(Adam)', '(Named)', '(Creature)', '(Living)', '(Name)'],
                'interpretation': 'From ground substrate, Source formed all land-beast and aerial-creature types and executed transfer function to Adam domain. Purpose: evaluate naming function capability. Adam successfully assigned identity labels to all autonomous P(t) maintenance entities.'
            },
            20: {
                'spl': 'ADA GAV NAM KAT FUL AIR BES FIE ADA FOU HELMET',
                'components': ['(Adam)', '(Gave)', '(Names)', '(Cattle)', '(Fowl)', '(Air)', '(Beast)', '(Field)', '(Adam)', '(Found)', '(Help-Meet)'],
                'interpretation': 'Adam executed identity label assignment for domesticated creatures, aerial types, and wild beasts. However, discovery function failed: no compatible support agent located among creature set for Adam.'
            },
            21: {
                'spl': 'GUG CAU DESLE FAL UPO ADA SLE TOK RIB CLO FLE INS',
                'components': ['(Source)', '(Caused)', '(Deep-Sleep)', '(Fall)', '(Upon)', '(Adam)', '(Slept)', '(Took)', '(Rib)', '(Closed)', '(Flesh)', '(Instead)'],
                'interpretation': 'The Source initiated state change triggering zero-consciousness state (suspended agent activity) upon Adam. During suspension, Source extracted structural component and executed sealing function (boundary restoration) using flesh material as replacement.'
            },
            22: {
                'spl': 'RIB TOK ADA GUG ING WOM BRO ADA',
                'components': ['(Rib)', '(Taken)', '(Adam)', '(Source)', '(Made)', '(Woman)', '(Brought)', '(Adam)'],
                'interpretation': 'Using the structural component extracted from Adam, the Source executed creation function generating the complementary agent type B (C_Formalizer_B / Woman) and transferred her to Adam domain.'
            },
            23: {
                'spl': 'ADA UZT BON BON FLE FLE SHA NAM WOM TAK MAN',
                'components': ['(Adam)', '(Said)', '(Bone)', '(Bones)', '(Flesh)', '(Flesh)', '(Shall)', '(Named)', '(Woman)', '(Taken)', '(Man)'],
                'interpretation': 'Adam declared: structural correspondence detected (bone of my bones, flesh of my flesh). Future certainty modal applied: she shall receive identity label Woman (WOM) because extraction function sourced her from Man (MAN). Structural and material continuity acknowledged.'
            },
            24: {
                'spl': 'THE MAN LEV FAT MOT CLE WIF ONFLE',
                'components': ['(Therefore)', '(Man)', '(Leave)', '(Father)', '(Mother)', '(Cleave)', '(Wife)', '(One-Flesh)'],
                'interpretation': 'Causal consequence principle established: Man shall execute departure function (bond breaking) from source lineage agents (father and mother) to execute bonding function with bonded female agent (wife), creating unified pair-bond state (merged agent structure).'
            },
            25: {
                'spl': 'BOT NAK ADA WIF NASH',
                'components': ['(Both)', '(Naked)', '(Adam)', '(Wife)', '(Not-Ashamed)'],
                'interpretation': 'The dual agents existed in unprotected state (no boundary layer) - both Adam and bonded female agent. However, zero-shame state maintained (pre-knowledge innocence). This is pre-λ awareness condition.'
            },
        }

        return encodings.get(verse_num, {
            'spl': '[ENCODING PENDING]',
            'components': [],
            'interpretation': 'Encoding not yet defined for this verse.'
        })

    def process_genesis_chapter_2(self, genesis_data: Dict) -> str:
        """Process Genesis Chapter 2 and return formatted markdown."""
        output_lines = []
        output_lines.append("# Genesis Chapter 2: Primal Logic Rework")
        output_lines.append("")
        output_lines.append("**Phase I: The Garden Domain and C_Formalizer Agent Initialization**")
        output_lines.append("")
        output_lines.append("---")
        output_lines.append("")

        # Find Chapter 2
        chapter_2 = None
        for chapter in genesis_data['chapters']:
            if chapter['chapter'] == '2':
                chapter_2 = chapter
                break

        if not chapter_2:
            return "Error: Genesis Chapter 2 not found"

        # Process each verse
        for verse_data in chapter_2['verses']:
            verse_num = int(verse_data['verse'])
            verse_text = verse_data['text']

            # Get SPL encoding
            encoding = self.encode_genesis_2_verse(verse_num, verse_text)

            # Format output
            output_lines.append(f"### Genesis 2:{verse_num}")
            output_lines.append("")
            output_lines.append("**[Original KJV]**")
            output_lines.append(f"{verse_text}")
            output_lines.append("")
            output_lines.append("**[Reworked SPL]**")
            output_lines.append(f"{encoding['spl']}")
            output_lines.append("")
            output_lines.append("**[Symbolic Meaning]**")
            if encoding['components']:
                output_lines.append(f"{' '.join(encoding['components'])}")
                output_lines.append("")
            output_lines.append(f"*Interpretation:* {encoding['interpretation']}")
            output_lines.append("")
            output_lines.append("---")
            output_lines.append("")

        return '\n'.join(output_lines)


def main():
    """Main execution function for Genesis Chapter 2."""
    # Load Genesis data
    with open('/home/user/Bible-kjv/Genesis.json', 'r') as f:
        genesis_data = json.load(f)

    # Create processor
    processor = SPLProcessorGen2()

    # Process Genesis Chapter 2
    output = processor.process_genesis_chapter_2(genesis_data)

    # Write output
    output_file = '/home/user/Bible-kjv/PLR_OUTPUT/Genesis_Chapter_02.md'
    with open(output_file, 'w') as f:
        f.write(output)

    print(f"Genesis Chapter 2 PLR output written to: {output_file}")
    print(f"Total verses processed: 25")
    print(f"SPL encoding complete according to Master Axiomatic Blueprint v8.2")
    print(f"New vocabulary added: {len(SPLVocabularyGen2.GENESIS_2_WORDS)} words")


if __name__ == '__main__':
    main()
