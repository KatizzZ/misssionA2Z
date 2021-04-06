# import gettext

# print(gettext.gettext('hello world tr',locale='ja_JP'))
import babel
import gettext
# from babel.dates import format_date, format_datetime
import babel.dates as bd
import datetime
_ = gettext.gettext
print(_('This is a translatable string.'))
print(_('Hello world.'))

print(bd.format_date(datetime.now()),locale='ja_JP')

# ro = gettext.translation('messages', localedir='../translations', languages=['de_DE'])
# ro.install()

# import locale
# import os

# current_locale, encoding = locale.getdefaultlocale()
# print(current_locale)
# locale_path = 'translations/locale'
# # language = gettext.translation ('brainz', locale_path, [current_locale] )
# # locale_path = '../translations' + 'de_DE' + '/LC_MESSAGES/'
# language = gettext.translation ('messages','Python/translations/locale/de_DE/LC_MESSAGES', 'de_DE' )
# # Python/translations/locale/de_DE/LC_MESSAGES/messages.mo
# language.install()
# print(_('This is a translatable string.'))
# print(_('Hello world.'))