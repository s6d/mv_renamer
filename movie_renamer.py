#!/usr/bin/python
#encoding:utf-8
#
# This program does a Google search for "quick and dirty" and returns
# 50 results.
#

#import sys
#import os
#from os.path import split, join, isfile, isdir
    

import re
import win32file
import sys
import os
import traceback
from xgoogle.search import GoogleSearch, SearchError

TRASH = ['ru','rus','en','eng',	'dvdrip', 'tvrip']

find_sites = ['imdb.com/title/tt', 'kinopoisk.ru/level']
allow_sites = ['rutor.org', 'bigtorrent.org', 'UaTracker.net', 'opensharing.org','uatracker.net','streamzone.org','www.torrentino.com']
#clean_name = [
#        'ru(s|)', 'en(g|)',
#        '((\(|)(cam|dvd|tv|sat|bd|hd)rip)|TS|PROPER(|S)(\)|)']

clean_name = [
        '((\.|_|)(DC|D|O)(\.|)|)(\(|)((cam|dvd|tv|sat|bd|hd|)(rip|scr|ts|TeleSync(h|)))(\)|).*|\.(RU(S|))\.|\.(EN(G|))\.',
        '(\[|\]|\(|\)|\.\.\.)', '(г\.\,.*)', '(xvid|divx|ac3)', '(\.avi|\.mkv)',
        'Скачать|фильм(ы|)|бесплатно|художественный', '&quot;', 'торрент', 'OpenSharing.ORG ::', 'Просмотр', 'темы',
        'Download', 'RuTor.Org ::', '(Bit|)Torrent','»', 'Торрент','\"' ]

trash_connect = [
        '<b>', '</b>', ' ']



def fail(s):
	print (s)
	sys.exit(1)

def main(argv):
	if len(argv) == 0:
		fail('Not enough args')
	filepath, filename = os.path.split(argv[0])
	title = search_by_filename(filename)
	title0 ,title1 = title.split('/')

	if title == None:
		alternative_search()

	print 'old name: ', argv[0],  'new name ru: ', title0 ,  'new name en: ', title1
#        path = args[0];
#        print path
#	return title

def alternative_search():

	return

def file_opertion():
	
	return


def search_by_filename(args):
	args_e=args.encode('utf8')
	try:
		gs = GoogleSearch('"' + args_e + '"')
		gs.results_per_page = 50
		results = gs.get_results()
		for res in results:
			if re_math_sites(allow_sites,res.url.encode('utf8')):
				if re_math_sites(args_e,res.desc.encode('utf8')):
					return clean_result(res.title.encode('utf8'))

	except SearchError, e:
		print "Search failed: %s" % e
#    return

def re_math_sites(argv1,argv2):
	patt = ur'%s' % '|'.join(argv1)
	if re.search(patt, argv2):
		return True
	else:
		return False

def clean_result(str):
    trash_re = '|'.join(r'%s' % t for t in clean_name)
    str = re.sub('(?i)' + trash_re, '', str)
    return str.strip()


if __name__=='__main__':
#    sys.exit(main())
#    input()

	try:
		main(sys.argv[1:])
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		traceback.print_exception(exc_type, exc_value, exc_traceback,file=sys.stdout)
		input()
