from biblemate import config
from biblemate.ui.selection_dialog import TerminalModeDialogs
from agentmake.plugins.uba.lib.BibleBooks import BibleBooks
from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
import re

DIALOGS = TerminalModeDialogs()

# shared dialogs

async def get_multiple_bibles(options, descriptions):
    select = await DIALOGS.getMultipleSelection(
        default_values=[config.default_bible],
        options=options,
        descriptions=descriptions,
        title="Bibles",
        text="Select versions to continue:"
    )
    return select if select else []

async def get_reference(verse_reference=True, exhaustiveReferences=False):
    result = await DIALOGS.getInputDialog(title="Bible Verse Reference", text="Enter a verse reference, e.g. John 3:16")
    if result:
        parser = BibleVerseParser(False)
        result = parser.extractExhaustiveReferencesReadable(result) if exhaustiveReferences else parser.extractAllReferencesReadable(result)
        if result and not verse_reference:
            result = re.sub(r":[\-0-9]+?;", ";", f"{result};")[:-1]
    if result:
        return result
    if not result:
        abbr = BibleBooks.abbrev["eng"]
        book = await DIALOGS.getValidOptions(
            default=str(config.last_book),
            options=[str(book) for book in range(1,67)],
            descriptions=[abbr[str(book)][-1] for book in range(1,67)],
            title="Bible Book",
            text="Select a book to continue:"
        )
        if not book:
            return ""
        config.last_book = book = int(book)
        chapter = await DIALOGS.getValidOptions(
            default=str(config.last_chapter),
            options=[str(chapter) for chapter in range(1,BibleBooks.chapters[int(book)]+1)],
            title="Bible Chapter",
            text="Select a chapter to continue:"
        )
        if not chapter:
            return ""
        config.last_chapter = chapter = int(chapter)
        if verse_reference:
            verse = await DIALOGS.getValidOptions(
                default=str(config.last_verse),
                options=[str(verse) for verse in range(1,BibleBooks.verses[int(book)][int(chapter)]+1)],
                title="Bible Verse",
                text="Select a verse to continue:"
            )
            if not verse:
                return ""
            config.last_verse = verse = int(verse)
            return f"{abbr[str(book)][0]} {chapter}:{verse}"
        return f"{abbr[str(book)][0]} {chapter}"

# dialogs for content retrieval

async def uba_bible(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Bible",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//bible/{select}/{result}" if result else ""

async def uba_chapter(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Bible",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    result = await get_reference(verse_reference=False)
    return f"//chapter/{select}/{result}" if result else ""

async def uba_compare(options, descriptions):
    select = await get_multiple_bibles(options, descriptions)
    if not select:
        return ""
    else:
        select = "_".join(select)
    result = await get_reference()
    return f"//uba/COMPARE:::{select}:::{result}" if result else ""

async def uba_compare_chapter(options, descriptions):
    select = await get_multiple_bibles(options, descriptions)
    if not select:
        return ""
    else:
        select = "_".join(select)
    result = await get_reference(verse_reference=False)
    return f"//uba/COMPARECHAPTER:::{select}:::{result}" if result else ""

async def uba_dictionary():
    result = await DIALOGS.getInputDialog(title="Search Dictionary", text="Enter a search item:")
    return f"//dictionary/{result.strip()}" if result and result.strip() else ""

async def uba_encyclopedia(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_encyclopedia,
        options=options,
        descriptions=descriptions,
        title="Encyclopedia",
        text="Select one of them to continue:"
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title=f"Search Encyclopedia - {select}", text="Enter a search item:")
    return f"//encyclopedia/{select}/{result.strip()}" if result and result.strip() else ""

async def uba_lexicon(options):
    select = await DIALOGS.getValidOptions(
        default=config.default_lexicon,
        options=options,
        title="Lexicon",
        text="Select one of them to continue:"
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title=f"Search Lexicon - {select}", text="Enter a search item:")
    return f"//lexicon/{select}/{result.strip()}" if result and result.strip() else ""

# TODO: dialogs for changing default modules