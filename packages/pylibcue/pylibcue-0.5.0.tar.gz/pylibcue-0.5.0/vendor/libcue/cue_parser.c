/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output, and Bison version.  */
#define YYBISON 30802

/* Bison version string.  */
#define YYBISON_VERSION "3.8.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* First part of user prologue.  */

/*
 * Copyright (c) 2004, 2005, 2006, 2007, Svend Sorensen
 * Copyright (c) 2009, 2010 Jochen Keil
 * For license terms, see the file COPYING in this distribution.
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "cd.h"
#include "time.h"

#ifdef YY_BUF_SIZE
#undef YY_BUF_SIZE
#endif
#define YY_BUF_SIZE 16384

#define YYDEBUG 1

char fnamebuf[PARSER_BUFFER];

/* debugging */
//int yydebug = 1;

extern int yylineno;
extern FILE* yyin;

static Cd *cd = NULL;
static Track *track = NULL;
static Track *prev_track = NULL;
static Cdtext *cdtext = NULL;
static Rem *rem = NULL;
static char *prev_filename = NULL;	/* last file in or before last track */
static char *cur_filename = NULL;	/* last file in the last track */
static char *new_filename = NULL;	/* last file in this track */

/* lexer interface */
typedef struct yy_buffer_state* YY_BUFFER_STATE;

int yylex(void);
void yyerror(const char*);
YY_BUFFER_STATE yy_scan_string(const char*);
YY_BUFFER_STATE yy_create_buffer(FILE*, int);
void yy_switch_to_buffer(YY_BUFFER_STATE);
void yy_delete_buffer(YY_BUFFER_STATE);

/* parser interface */
int yyparse(void);
Cd *cue_parse_file(FILE *fp);
Cd *cue_parse_string(const char*);


# ifndef YY_CAST
#  ifdef __cplusplus
#   define YY_CAST(Type, Val) static_cast<Type> (Val)
#   define YY_REINTERPRET_CAST(Type, Val) reinterpret_cast<Type> (Val)
#  else
#   define YY_CAST(Type, Val) ((Type) (Val))
#   define YY_REINTERPRET_CAST(Type, Val) ((Type) (Val))
#  endif
# endif
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

#include "cue_parser.h"
/* Symbol kind.  */
enum yysymbol_kind_t
{
  YYSYMBOL_YYEMPTY = -2,
  YYSYMBOL_YYEOF = 0,                      /* "end of file"  */
  YYSYMBOL_YYerror = 1,                    /* error  */
  YYSYMBOL_YYUNDEF = 2,                    /* "invalid token"  */
  YYSYMBOL_NUMBER = 3,                     /* NUMBER  */
  YYSYMBOL_STRING = 4,                     /* STRING  */
  YYSYMBOL_CATALOG = 5,                    /* CATALOG  */
  YYSYMBOL_CDTEXTFILE = 6,                 /* CDTEXTFILE  */
  YYSYMBOL_FFILE = 7,                      /* FFILE  */
  YYSYMBOL_BINARY = 8,                     /* BINARY  */
  YYSYMBOL_MOTOROLA = 9,                   /* MOTOROLA  */
  YYSYMBOL_AIFF = 10,                      /* AIFF  */
  YYSYMBOL_WAVE = 11,                      /* WAVE  */
  YYSYMBOL_MP3 = 12,                       /* MP3  */
  YYSYMBOL_FLAC = 13,                      /* FLAC  */
  YYSYMBOL_TRACK = 14,                     /* TRACK  */
  YYSYMBOL_AUDIO = 15,                     /* AUDIO  */
  YYSYMBOL_MODE1_2048 = 16,                /* MODE1_2048  */
  YYSYMBOL_MODE1_2352 = 17,                /* MODE1_2352  */
  YYSYMBOL_MODE2_2336 = 18,                /* MODE2_2336  */
  YYSYMBOL_MODE2_2048 = 19,                /* MODE2_2048  */
  YYSYMBOL_MODE2_2342 = 20,                /* MODE2_2342  */
  YYSYMBOL_MODE2_2332 = 21,                /* MODE2_2332  */
  YYSYMBOL_MODE2_2352 = 22,                /* MODE2_2352  */
  YYSYMBOL_TRACK_ISRC = 23,                /* TRACK_ISRC  */
  YYSYMBOL_FLAGS = 24,                     /* FLAGS  */
  YYSYMBOL_PRE = 25,                       /* PRE  */
  YYSYMBOL_DCP = 26,                       /* DCP  */
  YYSYMBOL_FOUR_CH = 27,                   /* FOUR_CH  */
  YYSYMBOL_SCMS = 28,                      /* SCMS  */
  YYSYMBOL_PREGAP = 29,                    /* PREGAP  */
  YYSYMBOL_INDEX = 30,                     /* INDEX  */
  YYSYMBOL_POSTGAP = 31,                   /* POSTGAP  */
  YYSYMBOL_TITLE = 32,                     /* TITLE  */
  YYSYMBOL_PERFORMER = 33,                 /* PERFORMER  */
  YYSYMBOL_SONGWRITER = 34,                /* SONGWRITER  */
  YYSYMBOL_COMPOSER = 35,                  /* COMPOSER  */
  YYSYMBOL_ARRANGER = 36,                  /* ARRANGER  */
  YYSYMBOL_MESSAGE = 37,                   /* MESSAGE  */
  YYSYMBOL_DISC_ID = 38,                   /* DISC_ID  */
  YYSYMBOL_GENRE = 39,                     /* GENRE  */
  YYSYMBOL_TOC_INFO1 = 40,                 /* TOC_INFO1  */
  YYSYMBOL_TOC_INFO2 = 41,                 /* TOC_INFO2  */
  YYSYMBOL_UPC_EAN = 42,                   /* UPC_EAN  */
  YYSYMBOL_ISRC = 43,                      /* ISRC  */
  YYSYMBOL_SIZE_INFO = 44,                 /* SIZE_INFO  */
  YYSYMBOL_DATE = 45,                      /* DATE  */
  YYSYMBOL_XXX_GENRE = 46,                 /* XXX_GENRE  */
  YYSYMBOL_XXX_DISCID = 47,                /* XXX_DISCID  */
  YYSYMBOL_XXX_COMPOSER = 48,              /* XXX_COMPOSER  */
  YYSYMBOL_REPLAYGAIN_ALBUM_GAIN = 49,     /* REPLAYGAIN_ALBUM_GAIN  */
  YYSYMBOL_REPLAYGAIN_ALBUM_PEAK = 50,     /* REPLAYGAIN_ALBUM_PEAK  */
  YYSYMBOL_REPLAYGAIN_TRACK_GAIN = 51,     /* REPLAYGAIN_TRACK_GAIN  */
  YYSYMBOL_REPLAYGAIN_TRACK_PEAK = 52,     /* REPLAYGAIN_TRACK_PEAK  */
  YYSYMBOL_COMMENT = 53,                   /* COMMENT  */
  YYSYMBOL_DISCNUMBER = 54,                /* DISCNUMBER  */
  YYSYMBOL_TOTALDISCS = 55,                /* TOTALDISCS  */
  YYSYMBOL_56_n_ = 56,                     /* '\n'  */
  YYSYMBOL_57_ = 57,                       /* ':'  */
  YYSYMBOL_YYACCEPT = 58,                  /* $accept  */
  YYSYMBOL_cuefile = 59,                   /* cuefile  */
  YYSYMBOL_new_cd = 60,                    /* new_cd  */
  YYSYMBOL_global_statements = 61,         /* global_statements  */
  YYSYMBOL_global_statement = 62,          /* global_statement  */
  YYSYMBOL_track_data = 63,                /* track_data  */
  YYSYMBOL_track_list = 64,                /* track_list  */
  YYSYMBOL_track = 65,                     /* track  */
  YYSYMBOL_file_format = 66,               /* file_format  */
  YYSYMBOL_new_track = 67,                 /* new_track  */
  YYSYMBOL_track_def = 68,                 /* track_def  */
  YYSYMBOL_track_mode = 69,                /* track_mode  */
  YYSYMBOL_track_statements = 70,          /* track_statements  */
  YYSYMBOL_track_statement = 71,           /* track_statement  */
  YYSYMBOL_track_flags = 72,               /* track_flags  */
  YYSYMBOL_track_flag = 73,                /* track_flag  */
  YYSYMBOL_cdtext = 74,                    /* cdtext  */
  YYSYMBOL_cdtext_item = 75,               /* cdtext_item  */
  YYSYMBOL_time = 76,                      /* time  */
  YYSYMBOL_rem = 77,                       /* rem  */
  YYSYMBOL_rem_item = 78                   /* rem_item  */
};
typedef enum yysymbol_kind_t yysymbol_kind_t;




#ifdef short
# undef short
#endif

/* On compilers that do not define __PTRDIFF_MAX__ etc., make sure
   <limits.h> and (if available) <stdint.h> are included
   so that the code can choose integer types of a good width.  */

#ifndef __PTRDIFF_MAX__
# include <limits.h> /* INFRINGES ON USER NAME SPACE */
# if defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stdint.h> /* INFRINGES ON USER NAME SPACE */
#  define YY_STDINT_H
# endif
#endif

/* Narrow types that promote to a signed type and that can represent a
   signed or unsigned integer of at least N bits.  In tables they can
   save space and decrease cache pressure.  Promoting to a signed type
   helps avoid bugs in integer arithmetic.  */

#ifdef __INT_LEAST8_MAX__
typedef __INT_LEAST8_TYPE__ yytype_int8;
#elif defined YY_STDINT_H
typedef int_least8_t yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef __INT_LEAST16_MAX__
typedef __INT_LEAST16_TYPE__ yytype_int16;
#elif defined YY_STDINT_H
typedef int_least16_t yytype_int16;
#else
typedef short yytype_int16;
#endif

/* Work around bug in HP-UX 11.23, which defines these macros
   incorrectly for preprocessor constants.  This workaround can likely
   be removed in 2023, as HPE has promised support for HP-UX 11.23
   (aka HP-UX 11i v2) only through the end of 2022; see Table 2 of
   <https://h20195.www2.hpe.com/V2/getpdf.aspx/4AA4-7673ENW.pdf>.  */
#ifdef __hpux
# undef UINT_LEAST8_MAX
# undef UINT_LEAST16_MAX
# define UINT_LEAST8_MAX 255
# define UINT_LEAST16_MAX 65535
#endif

#if defined __UINT_LEAST8_MAX__ && __UINT_LEAST8_MAX__ <= __INT_MAX__
typedef __UINT_LEAST8_TYPE__ yytype_uint8;
#elif (!defined __UINT_LEAST8_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST8_MAX <= INT_MAX)
typedef uint_least8_t yytype_uint8;
#elif !defined __UINT_LEAST8_MAX__ && UCHAR_MAX <= INT_MAX
typedef unsigned char yytype_uint8;
#else
typedef short yytype_uint8;
#endif

#if defined __UINT_LEAST16_MAX__ && __UINT_LEAST16_MAX__ <= __INT_MAX__
typedef __UINT_LEAST16_TYPE__ yytype_uint16;
#elif (!defined __UINT_LEAST16_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST16_MAX <= INT_MAX)
typedef uint_least16_t yytype_uint16;
#elif !defined __UINT_LEAST16_MAX__ && USHRT_MAX <= INT_MAX
typedef unsigned short yytype_uint16;
#else
typedef int yytype_uint16;
#endif

#ifndef YYPTRDIFF_T
# if defined __PTRDIFF_TYPE__ && defined __PTRDIFF_MAX__
#  define YYPTRDIFF_T __PTRDIFF_TYPE__
#  define YYPTRDIFF_MAXIMUM __PTRDIFF_MAX__
# elif defined PTRDIFF_MAX
#  ifndef ptrdiff_t
#   include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  endif
#  define YYPTRDIFF_T ptrdiff_t
#  define YYPTRDIFF_MAXIMUM PTRDIFF_MAX
# else
#  define YYPTRDIFF_T long
#  define YYPTRDIFF_MAXIMUM LONG_MAX
# endif
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM                                  \
  YY_CAST (YYPTRDIFF_T,                                 \
           (YYPTRDIFF_MAXIMUM < YY_CAST (YYSIZE_T, -1)  \
            ? YYPTRDIFF_MAXIMUM                         \
            : YY_CAST (YYSIZE_T, -1)))

#define YYSIZEOF(X) YY_CAST (YYPTRDIFF_T, sizeof (X))


/* Stored state numbers (used for stacks). */
typedef yytype_int8 yy_state_t;

/* State numbers in computations.  */
typedef int yy_state_fast_t;

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif


#ifndef YY_ATTRIBUTE_PURE
# if defined __GNUC__ && 2 < __GNUC__ + (96 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_PURE __attribute__ ((__pure__))
# else
#  define YY_ATTRIBUTE_PURE
# endif
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# if defined __GNUC__ && 2 < __GNUC__ + (7 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_UNUSED __attribute__ ((__unused__))
# else
#  define YY_ATTRIBUTE_UNUSED
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YY_USE(E) ((void) (E))
#else
# define YY_USE(E) /* empty */
#endif

/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
#if defined __GNUC__ && ! defined __ICC && 406 <= __GNUC__ * 100 + __GNUC_MINOR__
# if __GNUC__ * 100 + __GNUC_MINOR__ < 407
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")
# else
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")              \
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# endif
# define YY_IGNORE_MAYBE_UNINITIALIZED_END      \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

#if defined __cplusplus && defined __GNUC__ && ! defined __ICC && 6 <= __GNUC__
# define YY_IGNORE_USELESS_CAST_BEGIN                          \
    _Pragma ("GCC diagnostic push")                            \
    _Pragma ("GCC diagnostic ignored \"-Wuseless-cast\"")
# define YY_IGNORE_USELESS_CAST_END            \
    _Pragma ("GCC diagnostic pop")
#endif
#ifndef YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_END
#endif


#define YY_ASSERT(E) ((void) (0 && (E)))

#if !defined yyoverflow

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* !defined yyoverflow */

#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yy_state_t yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (YYSIZEOF (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (YYSIZEOF (yy_state_t) + YYSIZEOF (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYPTRDIFF_T yynewbytes;                                         \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * YYSIZEOF (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / YYSIZEOF (*yyptr);                        \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, YY_CAST (YYSIZE_T, (Count)) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYPTRDIFF_T yyi;                      \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  3
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   167

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  58
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  21
/* YYNRULES -- Number of rules.  */
#define YYNRULES  76
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  114

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   310


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK                     \
   ? YY_CAST (yysymbol_kind_t, yytranslate[YYX])        \
   : YYSYMBOL_YYUNDEF)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_int8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
      56,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    57,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,   138,   138,   142,   150,   151,   155,   156,   157,   158,
     159,   160,   164,   178,   179,   183,   187,   188,   189,   190,
     191,   192,   196,   220,   226,   227,   228,   229,   230,   231,
     232,   233,   237,   238,   242,   243,   244,   245,   246,   247,
     270,   271,   272,   276,   277,   281,   282,   283,   284,   288,
     292,   293,   294,   295,   296,   297,   298,   299,   300,   301,
     302,   303,   304,   308,   309,   313,   314,   315,   316,   320,
     321,   322,   323,   324,   325,   326,   327
};
#endif

/** Accessing symbol of state STATE.  */
#define YY_ACCESSING_SYMBOL(State) YY_CAST (yysymbol_kind_t, yystos[State])

#if YYDEBUG || 0
/* The user-facing name of the symbol whose (internal) number is
   YYSYMBOL.  No bounds checking.  */
static const char *yysymbol_name (yysymbol_kind_t yysymbol) YY_ATTRIBUTE_UNUSED;

/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "\"end of file\"", "error", "\"invalid token\"", "NUMBER", "STRING",
  "CATALOG", "CDTEXTFILE", "FFILE", "BINARY", "MOTOROLA", "AIFF", "WAVE",
  "MP3", "FLAC", "TRACK", "AUDIO", "MODE1_2048", "MODE1_2352",
  "MODE2_2336", "MODE2_2048", "MODE2_2342", "MODE2_2332", "MODE2_2352",
  "TRACK_ISRC", "FLAGS", "PRE", "DCP", "FOUR_CH", "SCMS", "PREGAP",
  "INDEX", "POSTGAP", "TITLE", "PERFORMER", "SONGWRITER", "COMPOSER",
  "ARRANGER", "MESSAGE", "DISC_ID", "GENRE", "TOC_INFO1", "TOC_INFO2",
  "UPC_EAN", "ISRC", "SIZE_INFO", "DATE", "XXX_GENRE", "XXX_DISCID",
  "XXX_COMPOSER", "REPLAYGAIN_ALBUM_GAIN", "REPLAYGAIN_ALBUM_PEAK",
  "REPLAYGAIN_TRACK_GAIN", "REPLAYGAIN_TRACK_PEAK", "COMMENT",
  "DISCNUMBER", "TOTALDISCS", "'\\n'", "':'", "$accept", "cuefile",
  "new_cd", "global_statements", "global_statement", "track_data",
  "track_list", "track", "file_format", "new_track", "track_def",
  "track_mode", "track_statements", "track_statement", "track_flags",
  "track_flag", "cdtext", "cdtext_item", "time", "rem", "rem_item", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-71)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-23)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int8 yypact[] =
{
     -71,     3,   -71,   -71,   110,   -52,     1,     2,     4,   -71,
     -71,   -71,   -71,   -71,   -71,   -71,   -71,   -71,   -71,   -71,
     -71,   -71,   -71,     5,     6,     8,   -71,   -71,   -71,   -71,
     -71,   -71,   -71,   -71,   -71,    -3,   -71,    -1,   -71,    17,
     -71,    18,   -71,   -30,   -29,     7,   -28,    15,    16,   -71,
      54,    55,    19,    20,   -71,   -71,   -71,   -71,   -71,   -71,
     -71,   -71,    21,   -71,   -71,   -71,    48,    24,    56,   -71,
      58,    70,    58,   -71,     0,   -71,   -71,   -71,   -71,   -71,
     -71,   -71,   -71,   -71,   -71,   -71,   -71,   -71,   -71,    25,
     -71,    26,   111,    57,    27,    58,    62,   -71,   -71,   -71,
     -71,   -71,   -71,   -71,   -71,   -71,    71,   -71,    63,   -71,
      64,   -71,   109,   -71
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int8 yydefact[] =
{
       3,     0,     4,     1,     0,     0,     0,     0,     0,    50,
      51,    52,    53,    54,    55,    56,    57,    58,    59,    60,
      61,    62,    69,     0,     0,     0,    70,    71,    72,    73,
      74,    75,    76,     5,    10,     2,    13,     0,     8,     0,
       9,     0,    11,     0,     0,     0,     0,     0,     0,    14,
       0,     0,     0,     0,     6,     7,    16,    17,    18,    19,
      20,    21,     0,    66,    67,    68,     0,     0,     0,    43,
       0,     0,     0,    41,     0,    32,    34,    35,    49,    65,
      12,    24,    25,    26,    27,    28,    29,    30,    31,     0,
      42,     0,     0,    63,     0,     0,     0,    33,    23,    37,
      45,    46,    47,    48,    36,    44,     0,    38,     0,    40,
       0,    39,     0,    64
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int8 yypgoto[] =
{
     -71,   -71,   -71,   -71,   -71,   116,   -71,    23,   -71,   -71,
     -71,   -71,   -71,   -15,   -71,   -71,   118,   -71,   -70,   119,
     -71
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int8 yydefgoto[] =
{
       0,     1,     2,     4,    33,    73,    35,    36,    62,    37,
      51,    89,    74,    75,    92,   105,    76,    39,    94,    77,
      41
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int8 yytable[] =
{
     -15,    67,    96,     3,    42,    43,    44,     8,    45,    46,
      47,   -22,    48,    50,   -15,    56,    57,    58,    59,    60,
      61,    52,    53,    68,    69,   108,    54,    55,    63,    70,
      71,    72,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    67,    66,    49,    97,
      91,    93,     8,    81,    82,    83,    84,    85,    86,    87,
      88,    64,    65,    95,   110,    78,    79,    80,    68,    69,
      90,    98,    99,   107,    70,    71,    72,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,    30,    31,
      32,     5,   113,     0,   106,     6,     7,     8,   109,   111,
      34,   112,    38,    40,   -22,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   100,   101,   102,   103,
       0,     0,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,     0,   104
};

static const yytype_int8 yycheck[] =
{
       0,     1,    72,     0,    56,     4,     4,     7,     4,     4,
       4,    14,     4,    14,    14,     8,     9,    10,    11,    12,
      13,     4,     4,    23,    24,    95,    56,    56,    56,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,    52,    53,    54,    55,     1,     3,    35,    74,
       4,     3,     7,    15,    16,    17,    18,    19,    20,    21,
      22,    56,    56,     3,     3,    56,    56,    56,    23,    24,
      56,    56,    56,    56,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,     1,     3,    -1,    57,     5,     6,     7,    56,    56,
       4,    57,     4,     4,    14,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    25,    26,    27,    28,
      -1,    -1,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,    52,    53,    54,    55,    -1,    56
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_int8 yystos[] =
{
       0,    59,    60,     0,    61,     1,     5,     6,     7,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,    52,
      53,    54,    55,    62,    63,    64,    65,    67,    74,    75,
      77,    78,    56,     4,     4,     4,     4,     4,     4,    65,
      14,    68,     4,     4,    56,    56,     8,     9,    10,    11,
      12,    13,    66,    56,    56,    56,     3,     1,    23,    24,
      29,    30,    31,    63,    70,    71,    74,    77,    56,    56,
      56,    15,    16,    17,    18,    19,    20,    21,    22,    69,
      56,     4,    72,     3,    76,     3,    76,    71,    56,    56,
      25,    26,    27,    28,    56,    73,    57,    56,    76,    56,
       3,    56,    57,     3
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr1[] =
{
       0,    58,    59,    60,    61,    61,    62,    62,    62,    62,
      62,    62,    63,    64,    64,    65,    66,    66,    66,    66,
      66,    66,    67,    68,    69,    69,    69,    69,    69,    69,
      69,    69,    70,    70,    71,    71,    71,    71,    71,    71,
      71,    71,    71,    72,    72,    73,    73,    73,    73,    74,
      75,    75,    75,    75,    75,    75,    75,    75,    75,    75,
      75,    75,    75,    76,    76,    77,    77,    77,    77,    78,
      78,    78,    78,    78,    78,    78,    78
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     3,     0,     0,     2,     3,     3,     1,     1,
       1,     2,     4,     1,     2,     3,     1,     1,     1,     1,
       1,     1,     0,     4,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     2,     1,     1,     3,     3,     3,     4,
       3,     1,     2,     0,     2,     1,     1,     1,     1,     3,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     5,     3,     3,     3,     3,     1,
       1,     1,     1,     1,     1,     1,     1
};


enum { YYENOMEM = -2 };

#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab
#define YYNOMEM         goto yyexhaustedlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (yychar == YYEMPTY)                                        \
      {                                                           \
        yychar = (Token);                                         \
        yylval = (Value);                                         \
        YYPOPSTACK (yylen);                                       \
        yystate = *yyssp;                                         \
        goto yybackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        yyerror (YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Backward compatibility with an undocumented macro.
   Use YYerror or YYUNDEF. */
#define YYERRCODE YYUNDEF


/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)




# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Kind, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
yy_symbol_value_print (FILE *yyo,
                       yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep)
{
  FILE *yyoutput = yyo;
  YY_USE (yyoutput);
  if (!yyvaluep)
    return;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
yy_symbol_print (FILE *yyo,
                 yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyo, "%s %s (",
             yykind < YYNTOKENS ? "token" : "nterm", yysymbol_name (yykind));

  yy_symbol_value_print (yyo, yykind, yyvaluep);
  YYFPRINTF (yyo, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yy_state_t *yybottom, yy_state_t *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yy_state_t *yyssp, YYSTYPE *yyvsp,
                 int yyrule)
{
  int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %d):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       YY_ACCESSING_SYMBOL (+yyssp[yyi + 1 - yynrhs]),
                       &yyvsp[(yyi + 1) - (yynrhs)]);
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args) ((void) 0)
# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif






/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg,
            yysymbol_kind_t yykind, YYSTYPE *yyvaluep)
{
  YY_USE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yykind, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/* Lookahead token kind.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;




/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    yy_state_fast_t yystate = 0;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus = 0;

    /* Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* Their size.  */
    YYPTRDIFF_T yystacksize = YYINITDEPTH;

    /* The state stack: array, bottom, top.  */
    yy_state_t yyssa[YYINITDEPTH];
    yy_state_t *yyss = yyssa;
    yy_state_t *yyssp = yyss;

    /* The semantic value stack: array, bottom, top.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs = yyvsa;
    YYSTYPE *yyvsp = yyvs;

  int yyn;
  /* The return value of yyparse.  */
  int yyresult;
  /* Lookahead symbol kind.  */
  yysymbol_kind_t yytoken = YYSYMBOL_YYEMPTY;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yychar = YYEMPTY; /* Cause a token to be read.  */

  goto yysetstate;


/*------------------------------------------------------------.
| yynewstate -- push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;


/*--------------------------------------------------------------------.
| yysetstate -- set current state (the top of the stack) to yystate.  |
`--------------------------------------------------------------------*/
yysetstate:
  YYDPRINTF ((stderr, "Entering state %d\n", yystate));
  YY_ASSERT (0 <= yystate && yystate < YYNSTATES);
  YY_IGNORE_USELESS_CAST_BEGIN
  *yyssp = YY_CAST (yy_state_t, yystate);
  YY_IGNORE_USELESS_CAST_END
  YY_STACK_PRINT (yyss, yyssp);

  if (yyss + yystacksize - 1 <= yyssp)
#if !defined yyoverflow && !defined YYSTACK_RELOCATE
    YYNOMEM;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYPTRDIFF_T yysize = yyssp - yyss + 1;

# if defined yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        yy_state_t *yyss1 = yyss;
        YYSTYPE *yyvs1 = yyvs;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * YYSIZEOF (*yyssp),
                    &yyvs1, yysize * YYSIZEOF (*yyvsp),
                    &yystacksize);
        yyss = yyss1;
        yyvs = yyvs1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        YYNOMEM;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yy_state_t *yyss1 = yyss;
        union yyalloc *yyptr =
          YY_CAST (union yyalloc *,
                   YYSTACK_ALLOC (YY_CAST (YYSIZE_T, YYSTACK_BYTES (yystacksize))));
        if (! yyptr)
          YYNOMEM;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YY_IGNORE_USELESS_CAST_BEGIN
      YYDPRINTF ((stderr, "Stack size increased to %ld\n",
                  YY_CAST (long, yystacksize)));
      YY_IGNORE_USELESS_CAST_END

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }
#endif /* !defined yyoverflow && !defined YYSTACK_RELOCATE */


  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;


/*-----------.
| yybackup.  |
`-----------*/
yybackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either empty, or end-of-input, or a valid lookahead.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token\n"));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = YYEOF;
      yytoken = YYSYMBOL_YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else if (yychar == YYerror)
    {
      /* The scanner already issued an error message, process directly
         to error recovery.  But do not keep the error token as
         lookahead, it is too special and may lead us to an endless
         loop in error recovery. */
      yychar = YYUNDEF;
      yytoken = YYSYMBOL_YYerror;
      goto yyerrlab1;
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);
  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  /* Discard the shifted token.  */
  yychar = YYEMPTY;
  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
  case 3: /* new_cd: %empty  */
                      {
		cd = cd_init();
		cdtext = cd_get_cdtext(cd);
		rem = cd_get_rem(cd);
	}
    break;

  case 6: /* global_statement: CATALOG STRING '\n'  */
                              { cd_set_catalog(cd, (yyvsp[-1].sval)); }
    break;

  case 7: /* global_statement: CDTEXTFILE STRING '\n'  */
                                 { cd_set_cdtextfile(cd, (yyvsp[-1].sval)); }
    break;

  case 12: /* track_data: FFILE STRING file_format '\n'  */
                                        {
		if (NULL != new_filename) {
			yyerror("too many files specified\n");
		}
		if (track && track_get_index(track, 1) == -1) {
			track_set_filename (track, (yyvsp[-2].sval));
		} else {
			new_filename = strncpy(fnamebuf, (yyvsp[-2].sval), sizeof(fnamebuf));
			new_filename[sizeof(fnamebuf) - 1] = '\0';
		}
	}
    break;

  case 22: /* new_track: %empty  */
                     {
		/* save previous track, to later set length */
		prev_track = track;

		track = cd_add_track(cd);
		if (prev_track == track)
			prev_track = NULL;
		cdtext = track_get_cdtext(track);
		rem = track_get_rem(track);

		cur_filename = new_filename;
		if (NULL != cur_filename)
			prev_filename = cur_filename;

		if (NULL == prev_filename)
			yyerror("no file specified for track");
		else
			track_set_filename(track, prev_filename);

		new_filename = NULL;
	}
    break;

  case 23: /* track_def: TRACK NUMBER track_mode '\n'  */
                                       {
		track_set_mode(track, (yyvsp[-1].ival));
	}
    break;

  case 37: /* track_statement: TRACK_ISRC STRING '\n'  */
                                 { track_set_isrc(track, (yyvsp[-1].sval)); }
    break;

  case 38: /* track_statement: PREGAP time '\n'  */
                           { track_set_zero_pre(track, (yyvsp[-1].ival)); }
    break;

  case 39: /* track_statement: INDEX NUMBER time '\n'  */
                                 {
		long prev_length;

		/* Set previous track length if it has not been set */
		if (NULL != prev_track && NULL == cur_filename
		    && track_get_length (prev_track) == -1) {
			/* track shares file with previous track */
			prev_length = (yyvsp[-1].ival) - track_get_start(prev_track);
			track_set_length(prev_track, prev_length);
		}

		if (1 == (yyvsp[-2].ival)) {
			/* INDEX 01 */
			track_set_start(track, (yyvsp[-1].ival));

			long idx00 = track_get_index (track, 0);

			if (idx00 != -1 && (yyvsp[-1].ival) != 0)
				track_set_zero_pre (track, (yyvsp[-1].ival) - idx00);
		}

		track_set_index (track, (yyvsp[-2].ival), (yyvsp[-1].ival));
	}
    break;

  case 40: /* track_statement: POSTGAP time '\n'  */
                            { track_set_zero_post(track, (yyvsp[-1].ival)); }
    break;

  case 44: /* track_flags: track_flags track_flag  */
                                 { track_set_flag(track, (yyvsp[0].ival)); }
    break;

  case 49: /* cdtext: cdtext_item STRING '\n'  */
                                  { cdtext_set ((yyvsp[-2].ival), (yyvsp[-1].sval), cdtext); }
    break;

  case 64: /* time: NUMBER ':' NUMBER ':' NUMBER  */
                                       { (yyval.ival) = time_msf_to_frame((yyvsp[-4].ival), (yyvsp[-2].ival), (yyvsp[0].ival)); }
    break;

  case 65: /* rem: rem_item STRING '\n'  */
                               { rem_set((yyvsp[-2].ival), (yyvsp[-1].sval), rem); }
    break;

  case 66: /* rem: XXX_GENRE STRING '\n'  */
                                { cdtext_set((yyvsp[-2].ival), (yyvsp[-1].sval), cdtext); }
    break;

  case 67: /* rem: XXX_DISCID STRING '\n'  */
                                 { cdtext_set((yyvsp[-2].ival), (yyvsp[-1].sval), cdtext); }
    break;

  case 68: /* rem: XXX_COMPOSER STRING '\n'  */
                                   { cdtext_set((yyvsp[-2].ival), (yyvsp[-1].sval), cdtext); }
    break;



      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", YY_CAST (yysymbol_kind_t, yyr1[yyn]), &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int yylhs = yyr1[yyn] - YYNTOKENS;
    const int yyi = yypgoto[yylhs] + *yyssp;
    yystate = (0 <= yyi && yyi <= YYLAST && yycheck[yyi] == *yyssp
               ? yytable[yyi]
               : yydefgoto[yylhs]);
  }

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYSYMBOL_YYEMPTY : YYTRANSLATE (yychar);
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
      yyerror (YY_("syntax error"));
    }

  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label yyerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;
  ++yynerrs;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  /* Pop stack until we find a state that shifts the error token.  */
  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYSYMBOL_YYerror;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYSYMBOL_YYerror)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  YY_ACCESSING_SYMBOL (yystate), yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", YY_ACCESSING_SYMBOL (yyn), yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturnlab;


/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturnlab;


/*-----------------------------------------------------------.
| yyexhaustedlab -- YYNOMEM (memory exhaustion) comes here.  |
`-----------------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  goto yyreturnlab;


/*----------------------------------------------------------.
| yyreturnlab -- parsing is finished, clean up and return.  |
`----------------------------------------------------------*/
yyreturnlab:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  YY_ACCESSING_SYMBOL (+*yyssp), yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif

  return yyresult;
}



/* lexer interface */

void yyerror (const char *s)
{
	#ifndef LIBCUE_QUIET_MODE
	fprintf(stderr, "%d: %s\n", yylineno, s);
	#endif
}

static void reset_static_vars()
{
	cd = NULL;
	track = NULL;
	prev_track = NULL;
	cdtext = NULL;
	rem = NULL;
	prev_filename = NULL;
	cur_filename = NULL;
	new_filename = NULL;
}

Cd *cue_parse_file(FILE *fp)
{
	YY_BUFFER_STATE buffer = NULL;

	yyin = fp;

	buffer = yy_create_buffer(yyin, YY_BUF_SIZE);

	yy_switch_to_buffer(buffer);

	Cd *ret_cd = NULL;

	yylineno = 1;
	if (0 == yyparse()) ret_cd = cd;
	else
	{
		ret_cd = NULL;
		if (cd) cd_delete(cd);
	}

	yy_delete_buffer(buffer);
	reset_static_vars();

	return ret_cd;
}

Cd *cue_parse_string(const char* string)
{
	YY_BUFFER_STATE buffer = NULL;

	buffer = yy_scan_string(string);

	Cd *ret_cd = NULL;

	yylineno = 1;
	if (0 == yyparse()) ret_cd = cd;
	else
	{
		ret_cd = NULL;
		if (cd) cd_delete(cd);
	}

	yy_delete_buffer(buffer);
	reset_static_vars();

	return ret_cd;
}
