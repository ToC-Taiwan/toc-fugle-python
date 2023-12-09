# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: realtime.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import entity_pb2 as entity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0erealtime.proto\x12\x14toc_python_forwarder\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0c\x65ntity.proto\"G\n\x10SnapshotResponse\x12\x33\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32%.toc_python_forwarder.SnapshotMessage\"0\n\x11YahooFinancePrice\x12\r\n\x05price\x18\x01 \x01(\x01\x12\x0c\n\x04last\x18\x02 \x01(\x01\"0\n\x11VolumeRankRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\"\xab\x03\n\x0fSnapshotMessage\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x10\n\x08\x65xchange\x18\x03 \x01(\t\x12\x0c\n\x04open\x18\x04 \x01(\x01\x12\x0c\n\x04high\x18\x05 \x01(\x01\x12\x0b\n\x03low\x18\x06 \x01(\x01\x12\r\n\x05\x63lose\x18\x07 \x01(\x01\x12\x11\n\ttick_type\x18\x08 \x01(\t\x12\x14\n\x0c\x63hange_price\x18\t \x01(\x01\x12\x13\n\x0b\x63hange_rate\x18\n \x01(\x01\x12\x13\n\x0b\x63hange_type\x18\x0b \x01(\t\x12\x15\n\raverage_price\x18\x0c \x01(\x01\x12\x0e\n\x06volume\x18\r \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0e \x01(\x03\x12\x0e\n\x06\x61mount\x18\x0f \x01(\x03\x12\x14\n\x0ctotal_amount\x18\x10 \x01(\x03\x12\x18\n\x10yesterday_volume\x18\x11 \x01(\x01\x12\x11\n\tbuy_price\x18\x12 \x01(\x01\x12\x12\n\nbuy_volume\x18\x13 \x01(\x01\x12\x12\n\nsell_price\x18\x14 \x01(\x01\x12\x13\n\x0bsell_volume\x18\x15 \x01(\x03\x12\x14\n\x0cvolume_ratio\x18\x16 \x01(\x01\"U\n\x17StockVolumeRankResponse\x12:\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32,.toc_python_forwarder.StockVolumeRankMessage\"\x8e\x04\n\x16StockVolumeRankMessage\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\n\n\x02ts\x18\x04 \x01(\x03\x12\x0c\n\x04open\x18\x05 \x01(\x01\x12\x0c\n\x04high\x18\x06 \x01(\x01\x12\x0b\n\x03low\x18\x07 \x01(\x01\x12\r\n\x05\x63lose\x18\x08 \x01(\x01\x12\x13\n\x0bprice_range\x18\t \x01(\x01\x12\x11\n\ttick_type\x18\n \x01(\x03\x12\x14\n\x0c\x63hange_price\x18\x0b \x01(\x01\x12\x13\n\x0b\x63hange_type\x18\x0c \x01(\x03\x12\x15\n\raverage_price\x18\r \x01(\x01\x12\x0e\n\x06volume\x18\x0e \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0f \x01(\x03\x12\x0e\n\x06\x61mount\x18\x10 \x01(\x03\x12\x14\n\x0ctotal_amount\x18\x11 \x01(\x03\x12\x18\n\x10yesterday_volume\x18\x12 \x01(\x03\x12\x14\n\x0cvolume_ratio\x18\x13 \x01(\x01\x12\x11\n\tbuy_price\x18\x14 \x01(\x01\x12\x12\n\nbuy_volume\x18\x15 \x01(\x03\x12\x12\n\nsell_price\x18\x16 \x01(\x01\x12\x13\n\x0bsell_volume\x18\x17 \x01(\x03\x12\x12\n\nbid_orders\x18\x18 \x01(\x03\x12\x13\n\x0b\x62id_volumes\x18\x19 \x01(\x03\x12\x12\n\nask_orders\x18\x1a \x01(\x03\x12\x13\n\x0b\x61sk_volumes\x18\x1b \x01(\x03\x32\x8c\x06\n\x15RealTimeDataInterface\x12W\n\x13GetAllStockSnapshot\x12\x16.google.protobuf.Empty\x1a&.toc_python_forwarder.SnapshotResponse\"\x00\x12g\n\x18GetStockSnapshotByNumArr\x12!.toc_python_forwarder.StockNumArr\x1a&.toc_python_forwarder.SnapshotResponse\"\x00\x12V\n\x13GetStockSnapshotTSE\x12\x16.google.protobuf.Empty\x1a%.toc_python_forwarder.SnapshotMessage\"\x00\x12V\n\x13GetStockSnapshotOTC\x12\x16.google.protobuf.Empty\x1a%.toc_python_forwarder.SnapshotMessage\"\x00\x12N\n\tGetNasdaq\x12\x16.google.protobuf.Empty\x1a\'.toc_python_forwarder.YahooFinancePrice\"\x00\x12T\n\x0fGetNasdaqFuture\x12\x16.google.protobuf.Empty\x1a\'.toc_python_forwarder.YahooFinancePrice\"\x00\x12n\n\x12GetStockVolumeRank\x12\'.toc_python_forwarder.VolumeRankRequest\x1a-.toc_python_forwarder.StockVolumeRankResponse\"\x00\x12k\n\x1aGetFutureSnapshotByCodeArr\x12#.toc_python_forwarder.FutureCodeArr\x1a&.toc_python_forwarder.SnapshotResponse\"\x00\x42\x06Z\x04./pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'realtime_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\004./pb'
  _globals['_SNAPSHOTRESPONSE']._serialized_start=83
  _globals['_SNAPSHOTRESPONSE']._serialized_end=154
  _globals['_YAHOOFINANCEPRICE']._serialized_start=156
  _globals['_YAHOOFINANCEPRICE']._serialized_end=204
  _globals['_VOLUMERANKREQUEST']._serialized_start=206
  _globals['_VOLUMERANKREQUEST']._serialized_end=254
  _globals['_SNAPSHOTMESSAGE']._serialized_start=257
  _globals['_SNAPSHOTMESSAGE']._serialized_end=684
  _globals['_STOCKVOLUMERANKRESPONSE']._serialized_start=686
  _globals['_STOCKVOLUMERANKRESPONSE']._serialized_end=771
  _globals['_STOCKVOLUMERANKMESSAGE']._serialized_start=774
  _globals['_STOCKVOLUMERANKMESSAGE']._serialized_end=1300
  _globals['_REALTIMEDATAINTERFACE']._serialized_start=1303
  _globals['_REALTIMEDATAINTERFACE']._serialized_end=2083
# @@protoc_insertion_point(module_scope)
