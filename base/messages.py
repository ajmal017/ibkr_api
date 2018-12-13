from enum import Enum
class Messages(object):
        class FieldType(Enum):
            INTEGER = 1
            STRING = 2,
            FLOAT = 3

        field_types = FieldType

        inbound = {
            'tick_price'                                    : 1,
            'tick_size'                                     : 2,
            'order_status'                                  : 3,
            'info_message'                                  : 4,
            'open_order'                                    : 5,
            'account_value'                                 : 6,
            'portfolio_value'                               : 7,
            'account_update_time'                           : 8,
            'next_valid_id'                                 : 9,
            'contract_data'                                 : 10,
            'execution_data'                                : 11,
            'market_depth'                                  : 12,
            'market_depth_l2'                               : 13,
            'news_bulletins'                                : 14,
            'managed_accounts'                              : 15,
            'receive_fa'                                    : 16,
            'historical_data'                               : 17,
            'bond_contract_data'                            : 18,
            'scanner_parameters'                            : 19,
            'scanner_data'                                  : 20,
            'tick_option_computation'                       : 21,
            'tick_generic'                                  : 45,
            'tick_string'                                   : 46,
            'tick_efp'                                      : 47,
            'current_time'                                  : 49,
            'real_time_bars'                                : 50,
            'fundamental_data'                              : 51,
            'contract_data_end'                             : 52,
            'open_order_end'                                : 53,
            'account_download_end'                          : 54,
            'execution_data_end'                            : 55,
            'delta_neutral_validation'                      : 56,
            'tick_snapshot_end'                             : 57,
            'market_data_type'                              : 58,
            'commission_report'                             : 59,
            'position_data'                                 : 61,
            'position_end'                                  : 62,
            'account_summary'                               : 63,
            'account_summary_end'                           : 64,
            'verify_message_api'                            : 65,
            'verify_completed'                              : 66,
            'display_group_list'                            : 67,
            'display_group_updated'                         : 68,
            'verify_and_auth_message_api'                   : 69,
            'verify_and_auth_completed'                     : 70,
            'position_multi'                                : 71,
            'position_multi_end'                            : 72,
            'account_update_multi'                          : 73,
            'account_update_multi_end'                      : 74,
            'security_definition_option_parameter'          : 75,
            'security_definition_option_parameter_end'      : 76,
            'soft_dollar_tiers'                             : 77,
            'family_codes'                                  : 78,
            'symbol_samples'                                : 79,
            'mkt_depth_exchanges'                           : 80,
            'tick_request_params'                           : 81,
            'smart_components'                              : 82,
            'news_article'                                  : 83,
            'tick_news'                                     : 84,
            'news_providers'                                : 85,
            'historical_news'                               : 86,
            'historical_news_end'                           : 87,
            'head_timestamp'                                : 88,
            'histogram_data'                                : 89,
            'historical_data_update'                        : 90,
            'reroute_market_data_req'                       : 91,
            'reroute_market_depth_req'                      : 92,
            'market_rule'                                   : 93,
            'pnl'                                           : 94,
            'pnl_single'                                    : 95,
            'historical_ticks'                              : 96,
            'historical_ticks_bid_ask'                      : 97,
            'historical_ticks_last'                         : 98,
            'tick_by_tick'                                  : 99,
            'order_bound'                                   : 100}

        outbound = {
            'request_market_data'                               : 1  ,
            'cancel_market_data'                                : 2  ,
            'place_order'                                       : 3  ,
            'cancel_order'                                      : 4  ,
            'request_open_orders'                               : 5  ,
            'request_account_data'                              : 6  ,
            'request_executions'                                : 7  ,
            'request_ids'                                       : 8  ,
            'request_contract_data'                             : 9  ,
            'request_market_depth'                              : 10 ,
            'cancel_market_depth'                               : 11 ,
            'request_news_bulletins'                            : 12 ,
            'cancel_news_bulletins'                             : 13 ,
            'set_server_loglevel'                               : 14 ,
            'request_auto_open_orders'                          : 15 ,
            'request_all_open_orders'                           : 16 ,
            'request_managed_accounts'                          : 17 ,
            'request_fa'                                        : 18 ,
            'replace_fa'                                        : 19 ,
            'request_historical_data'                           : 20 ,
            'exercise_options'                                  : 21 ,
            'request_scanner_subscription'                      : 22 ,
            'cancel_scanner_subscription'                       : 23 ,
            'request_scanner_parameters'                        : 24 ,
            'cancel_historical_data'                            : 25 ,
            'request_current_time'                              : 49 ,
            'request_real_time_bars'                            : 50 ,
            'cancel_real_time_bars'                             : 51 ,
            'request_fundamental_data'                          : 52 ,
            'cancel_fundamental_data'                           : 53 ,
            'request_calc_implied_volatility'                   : 54 ,
            'request_calc_option_price'                         : 55 ,
            'cancel_calc_implied_volat'                         : 56 ,
            'cancel_calc_option_price'                          : 57 ,
            'request_global_cancel'                             : 58 ,
            'request_market_data_type'                          : 59 ,
            'request_positions'                                 : 61 ,
            'request_account_summary'                           : 62 ,
            'cancel_account_summary'                            : 63 ,
            'cancel_positions'                                  : 64 ,
            'verify_request'                                    : 65 ,
            'verify_message'                                    : 66 ,
            'query_display_groups'                              : 67 ,
            'subscribe_to_group_events'                         : 68 ,
            'update_display_group'                              : 69 ,
            'unsubscribe_from_group_events'                     : 70 ,
            'start_api'                                         : 71 ,
            'verify_and_auth_request'                           : 72 ,
            'verify_and_auth_message'                           : 73 ,
            'request_positions_multi'                           : 74 ,
            'cancel_positions_multi'                            : 75 ,
            'request_account_updates_multi'                     : 76 ,
            'cancel_account_updates_multi'                      : 77 ,
            'request_security_definition_option_parameters'     : 78 ,
            'request_soft_dollar_tiers'                         : 79 ,
            'request_family_codes'                              : 80 ,
            'request_matching_symbols'                          : 81 ,
            'request_market_depth_exchanges'                    : 82 ,
            'request_smart_components'                          : 83 ,
            'request_news_article'                              : 84 ,
            'request_news_providers'                            : 85 ,
            'request_historical_news'                           : 86 ,
            'request_head_timestamp'                            : 87 ,
            'request_histogram_data'                            : 88 ,
            'cancel_histogram_data'                             : 89 ,
            'cancel_head_timestamp'                             : 90 ,
            'request_market_rule'                               : 91 ,
            'request_pnl'                                       : 92 ,
            'cancel_pnl'                                        : 93 ,
            'request_pnl_single'                                : 94 ,
            'cancel_pnl_single'                                 : 95 ,
            'request_historical_ticks'                          : 96 ,
            'request_tick_by_tick_data'                         : 97 ,
            'cancel_tick_by_tick_data'                          : 98
        }


        @staticmethod
        def parse_message(message: bytes):
            """ Parse message into a list of fields.
            The message is made of fields separated by NULL character"""
            fields = message.split(b"\0")
            fields[0] = int(fields[0])
            return tuple(fields[0:-1])

        @staticmethod
        def get_inbound_action(message_id):
            for action, action_id in Messages.inbound.items():
                if action_id == message_id:
                    return action