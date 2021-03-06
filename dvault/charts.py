from dvault import (bots)
from os import path
import string
import random


class dvine_chart:
    entry_point_base = ["dvine_chart"]

class dvine_chart_orders:
    entry_point_base = dvine_chart.entry_point_base + [
            '--chart-type', 'orders',
            '--with-order-status', 'filled' ]

class dvine_chart_accounts:
    entry_point_base = dvine_chart.entry_point_base + [
            '--chart-type', 'accounts'
            ]

class dvine_chart_all_returns:
    entry_point_base = dvine_chart_orders.entry_point_base + [
            '--orders-max-spam', 1 ]

class dvine_chart_recent_returns:
    entry_point_base = dvine_chart_orders.entry_point_base + [
            '--orders-max-spam', 2,
            '--orders-with-fill-after', 'now' ]



def _get_chart_cmd_series(name, base_args, discord_webhook_url, gen_args=[]):
    tmp_dir = path.join('/tmp','_get_chart_cmd_series' + ''.join(random.choice(string.digits) for i in range(5)) )
    pre_clean = [ 'rm', '-rf', tmp_dir ]
    create_dir = [ 'mkdir', '-p', tmp_dir]
    gen_chart = base_args + [
                '--plot-file', f'{tmp_dir}/{name}.png',
                '--output-file-list', f'{tmp_dir}/{name}.json' ] + gen_args

    notify = [ 'dsquire',
            '--embed-file-list', f'{tmp_dir}/{name}.json',
            '--discord-webhook-url', discord_webhook_url ]

    cleanup = [ 'rm', '-rf', tmp_dir ]

    return [pre_clean, create_dir, gen_chart, notify, cleanup ]

## us_equity universe, 3% std dev filter

class dvine_chart_us_equity_3Pct:
    tmp_dir = path.join('/tmp', 'dvine_chart_us_equity_3Pct' + ''.join(random.choice(string.digits) for i in range(5)) )
    bot = bots.dvine_us_equity_3Pct
    #discord_webhook_url = "https://discord.com/api/webhooks/999116224464158762/6lABNlrzm3oBucsxXjrfS8_ppAaqxUG5QH-OboKwAOpv3OVIT3s9ovJycSskjKwD7OYk" # to general channel on dvine server
    discord_webhook_url = "https://discordapp.com/api/webhooks/985010880771141663/iDyB-jVlcfvCdpIGm3cGlt7GLy3uoNozQCQIPihsF9BPQtVOSpeSYchit9SQRbo1gHo1" # to dvine channel on dstock server
    from_date_args = ['--from-date', '2022-06-08T00:00:00']

    base_args = \
            bot.strat.base_args + \
            bot.alpaca_args + \
            [
                '--plot-file', f'{tmp_dir}/dvine_chart_us_equity_3Pct.png',
                '--output-file-list', f'{tmp_dir}/dvine_chart_us_equity_3Pct.json',
                '--bot-name', bot.__name__ ]

class dvine_us_equity_3Pct_all_returns(dvine_chart_us_equity_3Pct):
    entry_point = _get_chart_cmd_series(
            'dvine_us_equity_3Pct_all_returns',
            dvine_chart_all_returns.entry_point_base +
                dvine_chart_us_equity_3Pct.bot.strat.base_args +
                dvine_chart_us_equity_3Pct.base_args +
                dvine_chart_us_equity_3Pct.from_date_args,
            dvine_chart_us_equity_3Pct.discord_webhook_url)

class dvine_us_equity_3Pct_recent_returns(dvine_chart_us_equity_3Pct):
    entry_point = _get_chart_cmd_series(
            'dvine_us_equity_3Pct_recent_returns',
            dvine_chart_recent_returns.entry_point_base +  dvine_chart_us_equity_3Pct.base_args,
            dvine_chart_us_equity_3Pct.discord_webhook_url)

class dvine_us_equity_3Pct_performance(dvine_chart_accounts):
    entry_point = _get_chart_cmd_series(
            'dvine_us_equity_3Pct_performance',
            dvine_chart_accounts.entry_point_base +
                dvine_chart_us_equity_3Pct.bot.strat.base_args +
                dvine_chart_us_equity_3Pct.base_args +
                dvine_chart_us_equity_3Pct.from_date_args + [
                    '--accounts-floor', 75000.00],
            dvine_chart_us_equity_3Pct.discord_webhook_url)


## us_equity universe, 5% std dev filter

class dvine_chart_us_equity_5Pct:
    bot = bots.dvine_us_equity_5Pct
    discord_webhook_url = "https://discord.com/api/webhooks/985015648923029544/tkru1WEjUkW3M_j1MrXOUQuQXZpbr0O6I7g84xyUFEcvfFbLlXDhnfpoVjDS7FwofdFc"
    base_args = \
            bot.strat.base_args + \
            bot.alpaca_args + \
            [
                '--bot-name', bot.__name__ ]
    from_date_args = ['--from-date', '2022-05-27T00:00:00']


class dvine_us_equity_5Pct_all_returns(dvine_chart_us_equity_5Pct):
    entry_point = _get_chart_cmd_series(
            'dvine_us_equity_5Pct_all_returns',
            dvine_chart_all_returns.entry_point_base +
                dvine_chart_us_equity_5Pct.bot.strat.base_args +
                dvine_chart_us_equity_5Pct.base_args +
                dvine_chart_us_equity_5Pct.from_date_args,
            dvine_chart_us_equity_5Pct.discord_webhook_url)

class dvine_us_equity_5Pct_recent_returns(dvine_chart_us_equity_5Pct):
    entry_point = _get_chart_cmd_series(
            'dvine_us_equity_5Pct_recent_returns',
            dvine_chart_recent_returns.entry_point_base +  dvine_chart_us_equity_5Pct.base_args,
            dvine_chart_us_equity_5Pct.discord_webhook_url)

class dvine_us_equity_5Pct_performance(dvine_chart_accounts):
    entry_point = _get_chart_cmd_series(
            'dvine_us_equity_5Pct_performance',
            dvine_chart_accounts.entry_point_base +
                dvine_chart_us_equity_5Pct.bot.strat.base_args +
                dvine_chart_us_equity_5Pct.base_args +
                dvine_chart_us_equity_5Pct.from_date_args + [
                        '--accounts-floor', 92500.00],
            dvine_chart_us_equity_5Pct.discord_webhook_url)
