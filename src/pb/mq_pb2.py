# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mq.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08mq.proto\x12\x14toc_python_forwarder\"f\n\x0c\x45ventMessage\x12\x11\n\tresp_code\x18\x01 \x01(\x03\x12\x12\n\nevent_code\x18\x02 \x01(\x03\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\r\n\x05\x65vent\x18\x04 \x01(\t\x12\x12\n\nevent_time\x18\x05 \x01(\t\"\xae\x03\n\x18StockRealTimeTickMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x11\n\tavg_price\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0c\n\x04high\x18\x06 \x01(\x01\x12\x0b\n\x03low\x18\x07 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x08 \x01(\x01\x12\x14\n\x0ctotal_amount\x18\t \x01(\x01\x12\x0e\n\x06volume\x18\n \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0b \x01(\x03\x12\x11\n\ttick_type\x18\x0c \x01(\x03\x12\x10\n\x08\x63hg_type\x18\r \x01(\x03\x12\x11\n\tprice_chg\x18\x0e \x01(\x01\x12\x0f\n\x07pct_chg\x18\x0f \x01(\x01\x12\x1a\n\x12\x62id_side_total_vol\x18\x10 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_vol\x18\x11 \x01(\x03\x12\x1a\n\x12\x62id_side_total_cnt\x18\x12 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_cnt\x18\x13 \x01(\x03\x12\x0f\n\x07suspend\x18\x14 \x01(\x08\x12\x10\n\x08simtrade\x18\x15 \x01(\x08\"\xda\x01\n\x1aStockRealTimeBidAskMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x11\n\tbid_price\x18\x03 \x03(\x01\x12\x12\n\nbid_volume\x18\x04 \x03(\x03\x12\x14\n\x0c\x64iff_bid_vol\x18\x05 \x03(\x03\x12\x11\n\task_price\x18\x06 \x03(\x01\x12\x12\n\nask_volume\x18\x07 \x03(\x03\x12\x14\n\x0c\x64iff_ask_vol\x18\x08 \x03(\x03\x12\x0f\n\x07suspend\x18\t \x01(\x08\x12\x10\n\x08simtrade\x18\n \x01(\x08\"\x80\x03\n\x19\x46utureRealTimeTickMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x18\n\x10underlying_price\x18\x04 \x01(\x01\x12\x1a\n\x12\x62id_side_total_vol\x18\x05 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_vol\x18\x06 \x01(\x03\x12\x11\n\tavg_price\x18\x07 \x01(\x01\x12\r\n\x05\x63lose\x18\x08 \x01(\x01\x12\x0c\n\x04high\x18\t \x01(\x01\x12\x0b\n\x03low\x18\n \x01(\x01\x12\x0e\n\x06\x61mount\x18\x0b \x01(\x01\x12\x14\n\x0ctotal_amount\x18\x0c \x01(\x01\x12\x0e\n\x06volume\x18\r \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0e \x01(\x03\x12\x11\n\ttick_type\x18\x0f \x01(\x03\x12\x10\n\x08\x63hg_type\x18\x10 \x01(\x03\x12\x11\n\tprice_chg\x18\x11 \x01(\x01\x12\x0f\n\x07pct_chg\x18\x12 \x01(\x01\x12\x10\n\x08simtrade\x18\x13 \x01(\x08\"\x92\x03\n\x1b\x46utureRealTimeBidAskMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x15\n\rbid_total_vol\x18\x03 \x01(\x03\x12\x15\n\rask_total_vol\x18\x04 \x01(\x03\x12\x11\n\tbid_price\x18\x05 \x03(\x01\x12\x12\n\nbid_volume\x18\x06 \x03(\x03\x12\x14\n\x0c\x64iff_bid_vol\x18\x07 \x03(\x03\x12\x11\n\task_price\x18\x08 \x03(\x01\x12\x12\n\nask_volume\x18\t \x03(\x03\x12\x14\n\x0c\x64iff_ask_vol\x18\n \x03(\x03\x12\x1f\n\x17\x66irst_derived_bid_price\x18\x0b \x01(\x01\x12\x1f\n\x17\x66irst_derived_ask_price\x18\x0c \x01(\x01\x12\x1d\n\x15\x66irst_derived_bid_vol\x18\r \x01(\x03\x12\x1d\n\x15\x66irst_derived_ask_vol\x18\x0e \x01(\x03\x12\x18\n\x10underlying_price\x18\x0f \x01(\x01\x12\x10\n\x08simtrade\x18\x10 \x01(\x08\"A\n\x0eOrderStatusArr\x12/\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.toc_python_forwarder.OrderStatus\"\x82\x01\n\x0bOrderStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x10\n\x08quantity\x18\x05 \x01(\x03\x12\x10\n\x08order_id\x18\x06 \x01(\t\x12\x12\n\norder_time\x18\x07 \x01(\tB\x06Z\x04./pbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mq_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\004./pb'
  _EVENTMESSAGE._serialized_start=34
  _EVENTMESSAGE._serialized_end=136
  _STOCKREALTIMETICKMESSAGE._serialized_start=139
  _STOCKREALTIMETICKMESSAGE._serialized_end=569
  _STOCKREALTIMEBIDASKMESSAGE._serialized_start=572
  _STOCKREALTIMEBIDASKMESSAGE._serialized_end=790
  _FUTUREREALTIMETICKMESSAGE._serialized_start=793
  _FUTUREREALTIMETICKMESSAGE._serialized_end=1177
  _FUTUREREALTIMEBIDASKMESSAGE._serialized_start=1180
  _FUTUREREALTIMEBIDASKMESSAGE._serialized_end=1582
  _ORDERSTATUSARR._serialized_start=1584
  _ORDERSTATUSARR._serialized_end=1649
  _ORDERSTATUS._serialized_start=1652
  _ORDERSTATUS._serialized_end=1782
# @@protoc_insertion_point(module_scope)
