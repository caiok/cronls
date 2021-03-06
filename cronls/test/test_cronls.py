# -*- coding: utf-8 -*-

import cronls.args
import cronls.cronls

# ==================================================================== #

class TestGetFiles:
	"""
	Tests for the crontab files processing

	TODO:
		- Tests for system cron file
		- Tests for cron directory

	Alas, this type of tests are not straighforward
	"""

	def test_1(self):
		input_args = cronls.args.parse_cmd_args(['--all'])
		l = cronls.cronls.get_crontab_files(input_args)
		# TODO...

# ==================================================================== #

class TestCronsProcessing:
	"""
	Tests for the cron rules processing
	"""

	def test_conversions(self):
		values = cronls.cronls.expand_rule(
			'10', field_type='', values_range=59, mapping={}, aliases={})
		assert values == set([10])

		values = cronls.cronls.expand_rule(
			'*', field_type='', values_range=59, mapping={}, aliases={})
		assert values == set(range(0, 59+1))

		values = cronls.cronls.expand_rule(
			'*/5', field_type='', values_range=59, mapping={}, aliases={})
		assert values == set(range(0, 59+1, 5))

		values = cronls.cronls.expand_rule(
			'*/10,5', field_type='', values_range=59, mapping={}, aliases={})
		assert values == set(list(range(0, 59 + 1, 10)) + [5])

		values = cronls.cronls.expand_rule(
			'mon-fri', field_type='', values_range=6, mapping=cronls.cronls.DAYS_OF_WEEK, aliases={})
		assert values == set([1, 2, 3, 4, 5])

		values = cronls.cronls.expand_rule(
			'mon-fri/2', field_type='', values_range=6, mapping=cronls.cronls.DAYS_OF_WEEK, aliases={})
		assert values == set([1, 3, 5])

		values = cronls.cronls.expand_rule(
			'5,mon,7', field_type='', values_range=6, mapping=cronls.cronls.DAYS_OF_WEEK, aliases=cronls.cronls.DAYS_OF_WEEK_ALIASES)
		assert values == set([0, 1, 5])

	def test_conversion_failures(self):
		# print(cronls.cronls.expand_rule('*/10,', field_type='', values_range=59, mapping={}, aliases={}))
		pass

# ==================================================================== #

if __name__ == '__main__':

	# Simple test for see if everything is ok

	import json

	input_args = cronls.args.parse_cmd_args(['--all'])
	l1 = cronls.cronls.get_crontab_files(input_args)
	#print(json.dumps(l1, indent=4))
	l2 = cronls.cronls.process_crontab(input_args)
	print(json.dumps(l2, indent=4))

	input_args = cronls.args.parse_cmd_args([])
	l1 = cronls.cronls.get_crontab_files(input_args)
	print(json.dumps(l1, indent=4))

	print(cronls.cronls.expand_rule('10', field_type='', values_range=59, mapping={}, aliases={}))
	print(cronls.cronls.expand_rule('*', field_type='', values_range=59, mapping={}, aliases={}))
	print(cronls.cronls.expand_rule('*/5', field_type='', values_range=59, mapping={}, aliases={}))
	#print(cronls.cronls.expand_rule('*/10,', field_type='', values_range=59, mapping={}, aliases={}))
	print(cronls.cronls.expand_rule('*/10,5', field_type='', values_range=59, mapping={}, aliases={}))
	print(cronls.cronls.expand_rule('mon-fri', field_type='', values_range=6, mapping=cronls.cronls.DAYS_OF_WEEK, aliases={}))
	print(cronls.cronls.expand_rule('mon-fri/2', field_type='', values_range=6, mapping=cronls.cronls.DAYS_OF_WEEK, aliases={}))
	print(cronls.cronls.expand_rule('5,mon,7', field_type='', values_range=6, mapping=cronls.cronls.DAYS_OF_WEEK, aliases=cronls.cronls.DAYS_OF_WEEK_ALIASES))