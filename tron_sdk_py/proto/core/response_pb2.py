# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tron_sdk_py/proto/core/response.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'tron_sdk_py/proto/core/response.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tron_sdk_py.proto.core import common_pb2 as tron__sdk__py_dot_proto_dot_core_dot_common__pb2
from tron_sdk_py.proto.core import chain_pb2 as tron__sdk__py_dot_proto_dot_core_dot_chain__pb2
from tron_sdk_py.proto.core import contract_pb2 as tron__sdk__py_dot_proto_dot_core_dot_contract__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%tron_sdk_py/proto/core/response.proto\x12\x08protocol\x1a#tron_sdk_py/proto/core/common.proto\x1a\"tron_sdk_py/proto/core/chain.proto\x1a%tron_sdk_py/proto/core/contract.proto\"\x84\x01\n\x0e\x42lockExtention\x12\x34\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x1e.protocol.TransactionExtention\x12+\n\x0c\x62lock_header\x18\x02 \x01(\x0b\x32\x15.protocol.BlockHeader\x12\x0f\n\x07\x62lockid\x18\x03 \x01(\x0c\"=\n\x12\x42lockListExtention\x12\'\n\x05\x62lock\x18\x01 \x03(\x0b\x32\x18.protocol.BlockExtention\"\xaa\x03\n\x11TransactionReturn\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x37\n\x04\x63ode\x18\x02 \x01(\x0e\x32).protocol.TransactionReturn.response_code\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"\xba\x02\n\rresponse_code\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0c\n\x08SIGERROR\x10\x01\x12\x1b\n\x17\x43ONTRACT_VALIDATE_ERROR\x10\x02\x12\x16\n\x12\x43ONTRACT_EXE_ERROR\x10\x03\x12\x12\n\x0e\x42\x41NDWITH_ERROR\x10\x04\x12\x19\n\x15\x44UP_TRANSACTION_ERROR\x10\x05\x12\x0f\n\x0bTAPOS_ERROR\x10\x06\x12\x1d\n\x19TOO_BIG_TRANSACTION_ERROR\x10\x07\x12 \n\x1cTRANSACTION_EXPIRATION_ERROR\x10\x08\x12\x0f\n\x0bSERVER_BUSY\x10\t\x12\x11\n\rNO_CONNECTION\x10\n\x12#\n\x1fNOT_ENOUGH_EFFECTIVE_CONNECTION\x10\x0b\x12\x0f\n\x0bOTHER_ERROR\x10\x14\"\x96\x01\n\x14TransactionExtention\x12*\n\x0btransaction\x18\x01 \x01(\x0b\x32\x15.protocol.Transaction\x12\x0c\n\x04txid\x18\x02 \x01(\x0c\x12\x17\n\x0f\x63onstant_result\x18\x03 \x03(\x0c\x12+\n\x06result\x18\x04 \x01(\x0b\x32\x1b.protocol.TransactionReturn\"3\n\x0bWitnessList\x12$\n\twitnesses\x18\x01 \x03(\x0b\x32\x11.protocol.Witness\"5\n\x0cProposalList\x12%\n\tproposals\x18\x01 \x03(\x0b\x32\x12.protocol.Proposal\"5\n\x0c\x45xchangeList\x12%\n\texchanges\x18\x01 \x03(\x0b\x32\x12.protocol.Exchange\">\n\x0e\x41ssetIssueList\x12,\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x1c.protocol.AssetIssueContract\"+\n\tBlockList\x12\x1e\n\x05\x62lock\x18\x01 \x03(\x0b\x32\x0f.protocol.Block\"=\n\x0fTransactionList\x12*\n\x0btransaction\x18\x01 \x03(\x0b\x32\x15.protocol.Transaction\"D\n\x18\x44\x65legatedResourceMessage\x12\x14\n\x0c\x66rom_address\x18\x01 \x01(\x0c\x12\x12\n\nto_address\x18\x02 \x01(\x0c\"O\n\x15\x44\x65legatedResourceList\x12\x36\n\x11\x64\x65legatedResource\x18\x01 \x03(\x0b\x32\x1b.protocol.DelegatedResource\">\n\x17\x41\x64\x64ressPrKeyPairMessage\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x12\n\nprivateKey\x18\x02 \x01(\t\"}\n\x14\x45\x61syTransferResponse\x12*\n\x0btransaction\x18\x01 \x01(\x0b\x32\x15.protocol.Transaction\x12+\n\x06result\x18\x02 \x01(\x0b\x32\x1b.protocol.TransactionReturn\x12\x0c\n\x04txid\x18\x03 \x01(\x0c\"a\n\x18SmartContractDataWrapper\x12/\n\x0esmart_contract\x18\x01 \x01(\x0b\x32\x17.protocol.SmartContract\x12\x14\n\x0cruntime_code\x18\x02 \x01(\x0c\"\xf0\x01\n\x13InternalTransaction\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x16\n\x0e\x63\x61ller_address\x18\x02 \x01(\x0c\x12\x1a\n\x12transferTo_address\x18\x03 \x01(\x0c\x12\x42\n\rcallValueInfo\x18\x04 \x03(\x0b\x32+.protocol.InternalTransaction.CallValueInfo\x12\x0c\n\x04note\x18\x05 \x01(\x0c\x12\x10\n\x08rejected\x18\x06 \x01(\x08\x1a\x33\n\rCallValueInfo\x12\x11\n\tcallValue\x18\x01 \x01(\x03\x12\x0f\n\x07tokenId\x18\x02 \x01(\t\"\xd5\x01\n\x0fResourceReceipt\x12\x14\n\x0c\x65nergy_usage\x18\x01 \x01(\x03\x12\x12\n\nenergy_fee\x18\x02 \x01(\x03\x12\x1b\n\x13origin_energy_usage\x18\x03 \x01(\x03\x12\x1a\n\x12\x65nergy_usage_total\x18\x04 \x01(\x03\x12\x11\n\tnet_usage\x18\x05 \x01(\x03\x12\x0f\n\x07net_fee\x18\x06 \x01(\x03\x12;\n\x06result\x18\x07 \x01(\x0e\x32+.protocol.Transaction.Result.contractResult\"\xf0\x05\n\x0fTransactionInfo\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0b\n\x03\x66\x65\x65\x18\x02 \x01(\x03\x12\x13\n\x0b\x62lockNumber\x18\x03 \x01(\x03\x12\x16\n\x0e\x62lockTimeStamp\x18\x04 \x01(\x03\x12\x16\n\x0e\x63ontractResult\x18\x05 \x03(\x0c\x12\x18\n\x10\x63ontract_address\x18\x06 \x01(\x0c\x12*\n\x07receipt\x18\x07 \x01(\x0b\x32\x19.protocol.ResourceReceipt\x12*\n\x03log\x18\x08 \x03(\x0b\x32\x1d.protocol.TransactionInfo.Log\x12.\n\x06result\x18\t \x01(\x0e\x32\x1e.protocol.TransactionInfo.code\x12\x12\n\nresMessage\x18\n \x01(\x0c\x12\x14\n\x0c\x61ssetIssueID\x18\x0e \x01(\t\x12\x17\n\x0fwithdraw_amount\x18\x0f \x01(\x03\x12\x17\n\x0funfreeze_amount\x18\x10 \x01(\x03\x12<\n\x15internal_transactions\x18\x11 \x03(\x0b\x32\x1d.protocol.InternalTransaction\x12 \n\x18\x65xchange_received_amount\x18\x12 \x01(\x03\x12&\n\x1e\x65xchange_inject_another_amount\x18\x13 \x01(\x03\x12(\n exchange_withdraw_another_amount\x18\x14 \x01(\x03\x12\x13\n\x0b\x65xchange_id\x18\x15 \x01(\x03\x12 \n\x18shielded_transaction_fee\x18\x16 \x01(\x03\x12\x0f\n\x07orderId\x18\x19 \x01(\x0c\x12\x31\n\x0corderDetails\x18\x1a \x03(\x0b\x32\x1b.protocol.MarketOrderDetail\x1a\x34\n\x03Log\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x0e\n\x06topics\x18\x02 \x03(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\x1e\n\x04\x63ode\x12\n\n\x06SUCESS\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\"\xb5\x01\n\x07Witness\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x11\n\tvoteCount\x18\x02 \x01(\x03\x12\x0e\n\x06pubKey\x18\x03 \x01(\x0c\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x15\n\rtotalProduced\x18\x05 \x01(\x03\x12\x13\n\x0btotalMissed\x18\x06 \x01(\x03\x12\x16\n\x0elatestBlockNum\x18\x07 \x01(\x03\x12\x15\n\rlatestSlotNum\x18\x08 \x01(\x03\x12\x0e\n\x06isJobs\x18\t \x01(\x08\"\xf0\x0f\n\x07\x41\x63\x63ount\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\x0c\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.protocol.AccountType\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0c\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x03\x12\x1d\n\x05votes\x18\x05 \x03(\x0b\x32\x0e.protocol.Vote\x12+\n\x05\x61sset\x18\x06 \x03(\x0b\x32\x1c.protocol.Account.AssetEntry\x12/\n\x07\x61ssetV2\x18\x38 \x03(\x0b\x32\x1e.protocol.Account.AssetV2Entry\x12(\n\x06\x66rozen\x18\x07 \x03(\x0b\x32\x18.protocol.Account.Frozen\x12\x11\n\tnet_usage\x18\x08 \x01(\x03\x12\x37\n/acquired_delegated_frozen_balance_for_bandwidth\x18) \x01(\x03\x12.\n&delegated_frozen_balance_for_bandwidth\x18* \x01(\x03\x12\x13\n\x0b\x63reate_time\x18\t \x01(\x03\x12\x1c\n\x14latest_opration_time\x18\n \x01(\x03\x12\x11\n\tallowance\x18\x0b \x01(\x03\x12\x1c\n\x14latest_withdraw_time\x18\x0c \x01(\x03\x12\x0c\n\x04\x63ode\x18\r \x01(\x0c\x12\x12\n\nis_witness\x18\x0e \x01(\x08\x12\x14\n\x0cis_committee\x18\x0f \x01(\x08\x12/\n\rfrozen_supply\x18\x10 \x03(\x0b\x32\x18.protocol.Account.Frozen\x12\x19\n\x11\x61sset_issued_name\x18\x11 \x01(\x0c\x12\x17\n\x0f\x61sset_issued_ID\x18\x39 \x01(\x0c\x12T\n\x1blatest_asset_operation_time\x18\x12 \x03(\x0b\x32/.protocol.Account.LatestAssetOperationTimeEntry\x12X\n\x1dlatest_asset_operation_timeV2\x18: \x03(\x0b\x32\x31.protocol.Account.LatestAssetOperationTimeV2Entry\x12\x16\n\x0e\x66ree_net_usage\x18\x13 \x01(\x03\x12\x46\n\x14\x66ree_asset_net_usage\x18\x14 \x03(\x0b\x32(.protocol.Account.FreeAssetNetUsageEntry\x12J\n\x16\x66ree_asset_net_usageV2\x18; \x03(\x0b\x32*.protocol.Account.FreeAssetNetUsageV2Entry\x12\x1b\n\x13latest_consume_time\x18\x15 \x01(\x03\x12 \n\x18latest_consume_free_time\x18\x16 \x01(\x03\x12\x12\n\naccount_id\x18\x17 \x01(\x0c\x12;\n\x10\x61\x63\x63ount_resource\x18\x1a \x01(\x0b\x32!.protocol.Account.AccountResource\x12\x10\n\x08\x63odeHash\x18\x1e \x01(\x0c\x12.\n\x10owner_permission\x18\x1f \x01(\x0b\x32\x14.protocol.Permission\x12\x30\n\x12witness_permission\x18  \x01(\x0b\x32\x14.protocol.Permission\x12/\n\x11\x61\x63tive_permission\x18! \x03(\x0b\x32\x14.protocol.Permission\x1a\x35\n\x06\x46rozen\x12\x16\n\x0e\x66rozen_balance\x18\x01 \x01(\x03\x12\x13\n\x0b\x65xpire_time\x18\x02 \x01(\x03\x1a,\n\nAssetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a.\n\x0c\x41ssetV2Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a?\n\x1dLatestAssetOperationTimeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x41\n\x1fLatestAssetOperationTimeV2Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x38\n\x16\x46reeAssetNetUsageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a:\n\x18\x46reeAssetNetUsageV2Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\xc3\x02\n\x0f\x41\x63\x63ountResource\x12\x14\n\x0c\x65nergy_usage\x18\x01 \x01(\x03\x12;\n\x19\x66rozen_balance_for_energy\x18\x02 \x01(\x0b\x32\x18.protocol.Account.Frozen\x12&\n\x1elatest_consume_time_for_energy\x18\x03 \x01(\x03\x12\x34\n,acquired_delegated_frozen_balance_for_energy\x18\x04 \x01(\x03\x12+\n#delegated_frozen_balance_for_energy\x18\x05 \x01(\x03\x12\x15\n\rstorage_limit\x18\x06 \x01(\x03\x12\x15\n\rstorage_usage\x18\x07 \x01(\x03\x12$\n\x1clatest_exchange_storage_time\x18\x08 \x01(\x03\"r\n\x11MarketOrderDetail\x12\x14\n\x0cmakerOrderId\x18\x01 \x01(\x0c\x12\x14\n\x0ctakerOrderId\x18\x02 \x01(\x0c\x12\x18\n\x10\x66illSellQuantity\x18\x03 \x01(\x03\x12\x17\n\x0f\x66illBuyQuantity\x18\x04 \x01(\x03\"\xd1\x02\n\x08Proposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x03\x12\x18\n\x10proposer_address\x18\x02 \x01(\x0c\x12\x36\n\nparameters\x18\x03 \x03(\x0b\x32\".protocol.Proposal.ParametersEntry\x12\x17\n\x0f\x65xpiration_time\x18\x04 \x01(\x03\x12\x13\n\x0b\x63reate_time\x18\x05 \x01(\x03\x12\x11\n\tapprovals\x18\x06 \x03(\x0c\x12\'\n\x05state\x18\x07 \x01(\x0e\x32\x18.protocol.Proposal.State\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"A\n\x05State\x12\x0b\n\x07PENDING\x10\x00\x12\x0f\n\x0b\x44ISAPPROVED\x10\x01\x12\x0c\n\x08\x41PPROVED\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\"\xb9\x01\n\x08\x45xchange\x12\x13\n\x0b\x65xchange_id\x18\x01 \x01(\x03\x12\x17\n\x0f\x63reator_address\x18\x02 \x01(\x0c\x12\x13\n\x0b\x63reate_time\x18\x03 \x01(\x03\x12\x16\n\x0e\x66irst_token_id\x18\x06 \x01(\x0c\x12\x1b\n\x13\x66irst_token_balance\x18\x07 \x01(\x03\x12\x17\n\x0fsecond_token_id\x18\x08 \x01(\x0c\x12\x1c\n\x14second_token_balance\x18\t \x01(\x03\"\xb9\x01\n\x11\x44\x65legatedResource\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x0c\x12\n\n\x02to\x18\x02 \x01(\x0c\x12$\n\x1c\x66rozen_balance_for_bandwidth\x18\x03 \x01(\x03\x12!\n\x19\x66rozen_balance_for_energy\x18\x04 \x01(\x03\x12!\n\x19\x65xpire_time_for_bandwidth\x18\x05 \x01(\x03\x12\x1e\n\x16\x65xpire_time_for_energy\x18\x06 \x01(\x03\"Z\n\x1d\x44\x65legatedResourceAccountIndex\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0c\x12\x14\n\x0c\x66romAccounts\x18\x02 \x03(\x0c\x12\x12\n\ntoAccounts\x18\x03 \x03(\x0c\"Q\n\x0fTransactionSign\x12*\n\x0btransaction\x18\x01 \x01(\x0b\x32\x15.protocol.Transaction\x12\x12\n\nprivateKey\x18\x02 \x01(\x0c\"\x81\x01\n\x0f\x43hainParameters\x12@\n\x0e\x63hainParameter\x18\x01 \x03(\x0b\x32(.protocol.ChainParameters.ChainParameter\x1a,\n\x0e\x43hainParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\"\xa0\x11\n\x08NodeInfo\x12\x14\n\x0c\x62\x65ginSyncNum\x18\x01 \x01(\x03\x12\r\n\x05\x62lock\x18\x02 \x01(\t\x12\x15\n\rsolidityBlock\x18\x03 \x01(\t\x12\x1b\n\x13\x63urrentConnectCount\x18\x04 \x01(\x05\x12\x1a\n\x12\x61\x63tiveConnectCount\x18\x05 \x01(\x05\x12\x1b\n\x13passiveConnectCount\x18\x06 \x01(\x05\x12\x11\n\ttotalFlow\x18\x07 \x01(\x03\x12\x31\n\x0cpeerInfoList\x18\x08 \x03(\x0b\x32\x1b.protocol.NodeInfo.PeerInfo\x12\x39\n\x0e\x63onfigNodeInfo\x18\t \x01(\x0b\x32!.protocol.NodeInfo.ConfigNodeInfo\x12\x33\n\x0bmachineInfo\x18\n \x01(\x0b\x32\x1e.protocol.NodeInfo.MachineInfo\x12H\n\x13\x63heatWitnessInfoMap\x18\x0b \x03(\x0b\x32+.protocol.NodeInfo.CheatWitnessInfoMapEntry\x1a:\n\x18\x43heatWitnessInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xcd\x04\n\x08PeerInfo\x12\x15\n\rlastSyncBlock\x18\x01 \x01(\t\x12\x11\n\tremainNum\x18\x02 \x01(\x03\x12\x1b\n\x13lastBlockUpdateTime\x18\x03 \x01(\x03\x12\x10\n\x08syncFlag\x18\x04 \x01(\x08\x12\x1f\n\x17headBlockTimeWeBothHave\x18\x05 \x01(\x03\x12\x18\n\x10needSyncFromPeer\x18\x06 \x01(\x08\x12\x16\n\x0eneedSyncFromUs\x18\x07 \x01(\x08\x12\x0c\n\x04host\x18\x08 \x01(\t\x12\x0c\n\x04port\x18\t \x01(\x05\x12\x0e\n\x06nodeId\x18\n \x01(\t\x12\x13\n\x0b\x63onnectTime\x18\x0b \x01(\x03\x12\x12\n\navgLatency\x18\x0c \x01(\x01\x12\x17\n\x0fsyncToFetchSize\x18\r \x01(\x05\x12\x1e\n\x16syncToFetchSizePeekNum\x18\x0e \x01(\x03\x12\x1e\n\x16syncBlockRequestedSize\x18\x0f \x01(\x05\x12\x15\n\runFetchSynNum\x18\x10 \x01(\x03\x12\x17\n\x0f\x62lockInPorcSize\x18\x11 \x01(\x05\x12\x1b\n\x13headBlockWeBothHave\x18\x12 \x01(\t\x12\x10\n\x08isActive\x18\x13 \x01(\x08\x12\r\n\x05score\x18\x14 \x01(\x05\x12\x11\n\tnodeCount\x18\x15 \x01(\x05\x12\x0e\n\x06inFlow\x18\x16 \x01(\x03\x12\x17\n\x0f\x64isconnectTimes\x18\x17 \x01(\x05\x12\x1d\n\x15localDisconnectReason\x18\x18 \x01(\t\x12\x1e\n\x16remoteDisconnectReason\x18\x19 \x01(\t\x1a\xe5\x03\n\x0e\x43onfigNodeInfo\x12\x13\n\x0b\x63odeVersion\x18\x01 \x01(\t\x12\x12\n\np2pVersion\x18\x02 \x01(\t\x12\x12\n\nlistenPort\x18\x03 \x01(\x05\x12\x16\n\x0e\x64iscoverEnable\x18\x04 \x01(\x08\x12\x16\n\x0e\x61\x63tiveNodeSize\x18\x05 \x01(\x05\x12\x17\n\x0fpassiveNodeSize\x18\x06 \x01(\x05\x12\x14\n\x0csendNodeSize\x18\x07 \x01(\x05\x12\x17\n\x0fmaxConnectCount\x18\x08 \x01(\x05\x12\x1d\n\x15sameIpMaxConnectCount\x18\t \x01(\x05\x12\x18\n\x10\x62\x61\x63kupListenPort\x18\n \x01(\x05\x12\x18\n\x10\x62\x61\x63kupMemberSize\x18\x0b \x01(\x05\x12\x16\n\x0e\x62\x61\x63kupPriority\x18\x0c \x01(\x05\x12\x11\n\tdbVersion\x18\r \x01(\x05\x12\x1c\n\x14minParticipationRate\x18\x0e \x01(\x05\x12\x17\n\x0fsupportConstant\x18\x0f \x01(\x08\x12\x14\n\x0cminTimeRatio\x18\x10 \x01(\x01\x12\x14\n\x0cmaxTimeRatio\x18\x11 \x01(\x01\x12 \n\x18\x61llowCreationOfContracts\x18\x12 \x01(\x03\x12\x1b\n\x13\x61llowAdaptiveEnergy\x18\x13 \x01(\x03\x1a\x8d\x05\n\x0bMachineInfo\x12\x13\n\x0bthreadCount\x18\x01 \x01(\x05\x12\x1b\n\x13\x64\x65\x61\x64LockThreadCount\x18\x02 \x01(\x05\x12\x10\n\x08\x63puCount\x18\x03 \x01(\x05\x12\x13\n\x0btotalMemory\x18\x04 \x01(\x03\x12\x12\n\nfreeMemory\x18\x05 \x01(\x03\x12\x0f\n\x07\x63puRate\x18\x06 \x01(\x01\x12\x13\n\x0bjavaVersion\x18\x07 \x01(\t\x12\x0e\n\x06osName\x18\x08 \x01(\t\x12\x17\n\x0fjvmTotalMemoery\x18\t \x01(\x03\x12\x15\n\rjvmFreeMemory\x18\n \x01(\x03\x12\x16\n\x0eprocessCpuRate\x18\x0b \x01(\x01\x12I\n\x12memoryDescInfoList\x18\x0c \x03(\x0b\x32-.protocol.NodeInfo.MachineInfo.MemoryDescInfo\x12Q\n\x16\x64\x65\x61\x64LockThreadInfoList\x18\r \x03(\x0b\x32\x31.protocol.NodeInfo.MachineInfo.DeadLockThreadInfo\x1a\x63\n\x0eMemoryDescInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08initSize\x18\x02 \x01(\x03\x12\x0f\n\x07useSize\x18\x03 \x01(\x03\x12\x0f\n\x07maxSize\x18\x04 \x01(\x03\x12\x0f\n\x07useRate\x18\x05 \x01(\x01\x1a\x8f\x01\n\x12\x44\x65\x61\x64LockThreadInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08lockName\x18\x02 \x01(\t\x12\x11\n\tlockOwner\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x11\n\tblockTime\x18\x05 \x01(\x03\x12\x10\n\x08waitTime\x18\x06 \x01(\x03\x12\x12\n\nstackTrace\x18\x07 \x01(\t\"\xf2\x02\n\x0bMarketOrder\x12\x10\n\x08order_id\x18\x01 \x01(\x0c\x12\x15\n\rowner_address\x18\x02 \x01(\x0c\x12\x13\n\x0b\x63reate_time\x18\x03 \x01(\x03\x12\x15\n\rsell_token_id\x18\x04 \x01(\x0c\x12\x1b\n\x13sell_token_quantity\x18\x05 \x01(\x03\x12\x14\n\x0c\x62uy_token_id\x18\x06 \x01(\x0c\x12\x1a\n\x12\x62uy_token_quantity\x18\x07 \x01(\x03\x12\"\n\x1asell_token_quantity_remain\x18\t \x01(\x03\x12\"\n\x1asell_token_quantity_return\x18\n \x01(\x03\x12*\n\x05state\x18\x0b \x01(\x0e\x32\x1b.protocol.MarketOrder.State\x12\x0c\n\x04prev\x18\x0c \x01(\x0c\x12\x0c\n\x04next\x18\r \x01(\x0c\"/\n\x05State\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\x0c\n\x08\x43\x41NCELED\x10\x02\"8\n\x0fMarketOrderList\x12%\n\x06orders\x18\x01 \x03(\x0b\x32\x15.protocol.MarketOrder\">\n\x0fMarketOrderPair\x12\x15\n\rsell_token_id\x18\x01 \x01(\x0c\x12\x14\n\x0c\x62uy_token_id\x18\x02 \x01(\x0c\"C\n\x13MarketOrderPairList\x12,\n\torderPair\x18\x01 \x03(\x0b\x32\x19.protocol.MarketOrderPair\"F\n\x0bMarketPrice\x12\x1b\n\x13sell_token_quantity\x18\x01 \x01(\x03\x12\x1a\n\x12\x62uy_token_quantity\x18\x02 \x01(\x03\"e\n\x0fMarketPriceList\x12\x15\n\rsell_token_id\x18\x01 \x01(\x0c\x12\x14\n\x0c\x62uy_token_id\x18\x02 \x01(\x0c\x12%\n\x06prices\x18\x03 \x03(\x0b\x32\x15.protocol.MarketPrice\"#\n\x0fNullifierResult\x12\x10\n\x08is_spent\x18\x01 \x01(\x08\"\xe5\x01\n\x11\x44\x65\x63ryptNotesTRC20\x12\x33\n\x07noteTxs\x18\x01 \x03(\x0b\x32\".protocol.DecryptNotesTRC20.NoteTx\x1a\x9a\x01\n\x06NoteTx\x12\x1c\n\x04note\x18\x01 \x01(\x0b\x32\x0e.protocol.Note\x12\x10\n\x08position\x18\x02 \x01(\x03\x12\x10\n\x08is_spent\x18\x03 \x01(\x08\x12\x0c\n\x04txid\x18\x04 \x01(\x0c\x12\r\n\x05index\x18\x05 \x01(\x05\x12\x11\n\tto_amount\x18\x06 \x01(\t\x12\x1e\n\x16transparent_to_address\x18\x07 \x01(\x0c\"I\n\x13TransactionInfoList\x12\x32\n\x0ftransactionInfo\x18\x01 \x03(\x0b\x32\x19.protocol.TransactionInfo\"\xe7\x02\n\x17TransactionApprovedList\x12\x15\n\rapproved_list\x18\x02 \x03(\x0c\x12\x38\n\x06result\x18\x04 \x01(\x0b\x32(.protocol.TransactionApprovedList.Result\x12\x33\n\x0btransaction\x18\x05 \x01(\x0b\x32\x1e.protocol.TransactionExtention\x1a\xc5\x01\n\x06Result\x12\x44\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x36.protocol.TransactionApprovedList.Result.response_code\x12\x0f\n\x07message\x18\x02 \x01(\t\"d\n\rresponse_code\x12\x0b\n\x07SUCCESS\x10\x00\x12\x1a\n\x16SIGNATURE_FORMAT_ERROR\x10\x01\x12\x19\n\x15\x43OMPUTE_ADDRESS_ERROR\x10\x02\x12\x0f\n\x0bOTHER_ERROR\x10\x14\"\xdf\x03\n\x15TransactionSignWeight\x12(\n\npermission\x18\x01 \x01(\x0b\x32\x14.protocol.Permission\x12\x15\n\rapproved_list\x18\x02 \x03(\x0c\x12\x16\n\x0e\x63urrent_weight\x18\x03 \x01(\x03\x12\x36\n\x06result\x18\x04 \x01(\x0b\x32&.protocol.TransactionSignWeight.Result\x12\x33\n\x0btransaction\x18\x05 \x01(\x0b\x32\x1e.protocol.TransactionExtention\x1a\xff\x01\n\x06Result\x12\x42\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x34.protocol.TransactionSignWeight.Result.response_code\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x9f\x01\n\rresponse_code\x12\x15\n\x11\x45NOUGH_PERMISSION\x10\x00\x12\x19\n\x15NOT_ENOUGH_PERMISSION\x10\x01\x12\x1a\n\x16SIGNATURE_FORMAT_ERROR\x10\x02\x12\x19\n\x15\x43OMPUTE_ADDRESS_ERROR\x10\x03\x12\x14\n\x10PERMISSION_ERROR\x10\x04\x12\x0f\n\x0bOTHER_ERROR\x10\x14\"\x93\x01\n\x08NodeList\x12&\n\x05nodes\x18\x01 \x03(\x0b\x32\x17.protocol.NodeList.Node\x1a_\n\x04Node\x12\x30\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1f.protocol.NodeList.Node.Address\x1a%\n\x07\x41\x64\x64ress\x12\x0c\n\x04host\x18\x01 \x01(\x0c\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\x87\x03\n\x11\x41\x63\x63ountNetMessage\x12\x13\n\x0b\x66reeNetUsed\x18\x01 \x01(\x03\x12\x14\n\x0c\x66reeNetLimit\x18\x02 \x01(\x03\x12\x0f\n\x07NetUsed\x18\x03 \x01(\x03\x12\x10\n\x08NetLimit\x18\x04 \x01(\x03\x12\x43\n\x0c\x61ssetNetUsed\x18\x05 \x03(\x0b\x32-.protocol.AccountNetMessage.AssetNetUsedEntry\x12\x45\n\rassetNetLimit\x18\x06 \x03(\x0b\x32..protocol.AccountNetMessage.AssetNetLimitEntry\x12\x15\n\rTotalNetLimit\x18\x07 \x01(\x03\x12\x16\n\x0eTotalNetWeight\x18\x08 \x01(\x03\x1a\x33\n\x11\x41ssetNetUsedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x34\n\x12\x41ssetNetLimitEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\x9f\x04\n\x16\x41\x63\x63ountResourceMessage\x12\x13\n\x0b\x66reeNetUsed\x18\x01 \x01(\x03\x12\x14\n\x0c\x66reeNetLimit\x18\x02 \x01(\x03\x12\x0f\n\x07NetUsed\x18\x03 \x01(\x03\x12\x10\n\x08NetLimit\x18\x04 \x01(\x03\x12H\n\x0c\x61ssetNetUsed\x18\x05 \x03(\x0b\x32\x32.protocol.AccountResourceMessage.AssetNetUsedEntry\x12J\n\rassetNetLimit\x18\x06 \x03(\x0b\x32\x33.protocol.AccountResourceMessage.AssetNetLimitEntry\x12\x15\n\rTotalNetLimit\x18\x07 \x01(\x03\x12\x16\n\x0eTotalNetWeight\x18\x08 \x01(\x03\x12\x12\n\nEnergyUsed\x18\r \x01(\x03\x12\x13\n\x0b\x45nergyLimit\x18\x0e \x01(\x03\x12\x18\n\x10TotalEnergyLimit\x18\x0f \x01(\x03\x12\x19\n\x11TotalEnergyWeight\x18\x10 \x01(\x03\x12\x13\n\x0bstorageUsed\x18\x15 \x01(\x03\x12\x14\n\x0cstorageLimit\x18\x16 \x01(\x03\x1a\x33\n\x11\x41ssetNetUsedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1a\x34\n\x12\x41ssetNetLimitEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tron_sdk_py.proto.core.response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ACCOUNT_ASSETENTRY']._loaded_options = None
  _globals['_ACCOUNT_ASSETENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNT_ASSETV2ENTRY']._loaded_options = None
  _globals['_ACCOUNT_ASSETV2ENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNT_LATESTASSETOPERATIONTIMEENTRY']._loaded_options = None
  _globals['_ACCOUNT_LATESTASSETOPERATIONTIMEENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNT_LATESTASSETOPERATIONTIMEV2ENTRY']._loaded_options = None
  _globals['_ACCOUNT_LATESTASSETOPERATIONTIMEV2ENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNT_FREEASSETNETUSAGEENTRY']._loaded_options = None
  _globals['_ACCOUNT_FREEASSETNETUSAGEENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNT_FREEASSETNETUSAGEV2ENTRY']._loaded_options = None
  _globals['_ACCOUNT_FREEASSETNETUSAGEV2ENTRY']._serialized_options = b'8\001'
  _globals['_PROPOSAL_PARAMETERSENTRY']._loaded_options = None
  _globals['_PROPOSAL_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_NODEINFO_CHEATWITNESSINFOMAPENTRY']._loaded_options = None
  _globals['_NODEINFO_CHEATWITNESSINFOMAPENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNTNETMESSAGE_ASSETNETUSEDENTRY']._loaded_options = None
  _globals['_ACCOUNTNETMESSAGE_ASSETNETUSEDENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNTNETMESSAGE_ASSETNETLIMITENTRY']._loaded_options = None
  _globals['_ACCOUNTNETMESSAGE_ASSETNETLIMITENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNTRESOURCEMESSAGE_ASSETNETUSEDENTRY']._loaded_options = None
  _globals['_ACCOUNTRESOURCEMESSAGE_ASSETNETUSEDENTRY']._serialized_options = b'8\001'
  _globals['_ACCOUNTRESOURCEMESSAGE_ASSETNETLIMITENTRY']._loaded_options = None
  _globals['_ACCOUNTRESOURCEMESSAGE_ASSETNETLIMITENTRY']._serialized_options = b'8\001'
  _globals['_BLOCKEXTENTION']._serialized_start=164
  _globals['_BLOCKEXTENTION']._serialized_end=296
  _globals['_BLOCKLISTEXTENTION']._serialized_start=298
  _globals['_BLOCKLISTEXTENTION']._serialized_end=359
  _globals['_TRANSACTIONRETURN']._serialized_start=362
  _globals['_TRANSACTIONRETURN']._serialized_end=788
  _globals['_TRANSACTIONRETURN_RESPONSE_CODE']._serialized_start=474
  _globals['_TRANSACTIONRETURN_RESPONSE_CODE']._serialized_end=788
  _globals['_TRANSACTIONEXTENTION']._serialized_start=791
  _globals['_TRANSACTIONEXTENTION']._serialized_end=941
  _globals['_WITNESSLIST']._serialized_start=943
  _globals['_WITNESSLIST']._serialized_end=994
  _globals['_PROPOSALLIST']._serialized_start=996
  _globals['_PROPOSALLIST']._serialized_end=1049
  _globals['_EXCHANGELIST']._serialized_start=1051
  _globals['_EXCHANGELIST']._serialized_end=1104
  _globals['_ASSETISSUELIST']._serialized_start=1106
  _globals['_ASSETISSUELIST']._serialized_end=1168
  _globals['_BLOCKLIST']._serialized_start=1170
  _globals['_BLOCKLIST']._serialized_end=1213
  _globals['_TRANSACTIONLIST']._serialized_start=1215
  _globals['_TRANSACTIONLIST']._serialized_end=1276
  _globals['_DELEGATEDRESOURCEMESSAGE']._serialized_start=1278
  _globals['_DELEGATEDRESOURCEMESSAGE']._serialized_end=1346
  _globals['_DELEGATEDRESOURCELIST']._serialized_start=1348
  _globals['_DELEGATEDRESOURCELIST']._serialized_end=1427
  _globals['_ADDRESSPRKEYPAIRMESSAGE']._serialized_start=1429
  _globals['_ADDRESSPRKEYPAIRMESSAGE']._serialized_end=1491
  _globals['_EASYTRANSFERRESPONSE']._serialized_start=1493
  _globals['_EASYTRANSFERRESPONSE']._serialized_end=1618
  _globals['_SMARTCONTRACTDATAWRAPPER']._serialized_start=1620
  _globals['_SMARTCONTRACTDATAWRAPPER']._serialized_end=1717
  _globals['_INTERNALTRANSACTION']._serialized_start=1720
  _globals['_INTERNALTRANSACTION']._serialized_end=1960
  _globals['_INTERNALTRANSACTION_CALLVALUEINFO']._serialized_start=1909
  _globals['_INTERNALTRANSACTION_CALLVALUEINFO']._serialized_end=1960
  _globals['_RESOURCERECEIPT']._serialized_start=1963
  _globals['_RESOURCERECEIPT']._serialized_end=2176
  _globals['_TRANSACTIONINFO']._serialized_start=2179
  _globals['_TRANSACTIONINFO']._serialized_end=2931
  _globals['_TRANSACTIONINFO_LOG']._serialized_start=2847
  _globals['_TRANSACTIONINFO_LOG']._serialized_end=2899
  _globals['_TRANSACTIONINFO_CODE']._serialized_start=2901
  _globals['_TRANSACTIONINFO_CODE']._serialized_end=2931
  _globals['_WITNESS']._serialized_start=2934
  _globals['_WITNESS']._serialized_end=3115
  _globals['_ACCOUNT']._serialized_start=3118
  _globals['_ACCOUNT']._serialized_end=5150
  _globals['_ACCOUNT_FROZEN']._serialized_start=4427
  _globals['_ACCOUNT_FROZEN']._serialized_end=4480
  _globals['_ACCOUNT_ASSETENTRY']._serialized_start=4482
  _globals['_ACCOUNT_ASSETENTRY']._serialized_end=4526
  _globals['_ACCOUNT_ASSETV2ENTRY']._serialized_start=4528
  _globals['_ACCOUNT_ASSETV2ENTRY']._serialized_end=4574
  _globals['_ACCOUNT_LATESTASSETOPERATIONTIMEENTRY']._serialized_start=4576
  _globals['_ACCOUNT_LATESTASSETOPERATIONTIMEENTRY']._serialized_end=4639
  _globals['_ACCOUNT_LATESTASSETOPERATIONTIMEV2ENTRY']._serialized_start=4641
  _globals['_ACCOUNT_LATESTASSETOPERATIONTIMEV2ENTRY']._serialized_end=4706
  _globals['_ACCOUNT_FREEASSETNETUSAGEENTRY']._serialized_start=4708
  _globals['_ACCOUNT_FREEASSETNETUSAGEENTRY']._serialized_end=4764
  _globals['_ACCOUNT_FREEASSETNETUSAGEV2ENTRY']._serialized_start=4766
  _globals['_ACCOUNT_FREEASSETNETUSAGEV2ENTRY']._serialized_end=4824
  _globals['_ACCOUNT_ACCOUNTRESOURCE']._serialized_start=4827
  _globals['_ACCOUNT_ACCOUNTRESOURCE']._serialized_end=5150
  _globals['_MARKETORDERDETAIL']._serialized_start=5152
  _globals['_MARKETORDERDETAIL']._serialized_end=5266
  _globals['_PROPOSAL']._serialized_start=5269
  _globals['_PROPOSAL']._serialized_end=5606
  _globals['_PROPOSAL_PARAMETERSENTRY']._serialized_start=5490
  _globals['_PROPOSAL_PARAMETERSENTRY']._serialized_end=5539
  _globals['_PROPOSAL_STATE']._serialized_start=5541
  _globals['_PROPOSAL_STATE']._serialized_end=5606
  _globals['_EXCHANGE']._serialized_start=5609
  _globals['_EXCHANGE']._serialized_end=5794
  _globals['_DELEGATEDRESOURCE']._serialized_start=5797
  _globals['_DELEGATEDRESOURCE']._serialized_end=5982
  _globals['_DELEGATEDRESOURCEACCOUNTINDEX']._serialized_start=5984
  _globals['_DELEGATEDRESOURCEACCOUNTINDEX']._serialized_end=6074
  _globals['_TRANSACTIONSIGN']._serialized_start=6076
  _globals['_TRANSACTIONSIGN']._serialized_end=6157
  _globals['_CHAINPARAMETERS']._serialized_start=6160
  _globals['_CHAINPARAMETERS']._serialized_end=6289
  _globals['_CHAINPARAMETERS_CHAINPARAMETER']._serialized_start=6245
  _globals['_CHAINPARAMETERS_CHAINPARAMETER']._serialized_end=6289
  _globals['_NODEINFO']._serialized_start=6292
  _globals['_NODEINFO']._serialized_end=8500
  _globals['_NODEINFO_CHEATWITNESSINFOMAPENTRY']._serialized_start=6706
  _globals['_NODEINFO_CHEATWITNESSINFOMAPENTRY']._serialized_end=6764
  _globals['_NODEINFO_PEERINFO']._serialized_start=6767
  _globals['_NODEINFO_PEERINFO']._serialized_end=7356
  _globals['_NODEINFO_CONFIGNODEINFO']._serialized_start=7359
  _globals['_NODEINFO_CONFIGNODEINFO']._serialized_end=7844
  _globals['_NODEINFO_MACHINEINFO']._serialized_start=7847
  _globals['_NODEINFO_MACHINEINFO']._serialized_end=8500
  _globals['_NODEINFO_MACHINEINFO_MEMORYDESCINFO']._serialized_start=8255
  _globals['_NODEINFO_MACHINEINFO_MEMORYDESCINFO']._serialized_end=8354
  _globals['_NODEINFO_MACHINEINFO_DEADLOCKTHREADINFO']._serialized_start=8357
  _globals['_NODEINFO_MACHINEINFO_DEADLOCKTHREADINFO']._serialized_end=8500
  _globals['_MARKETORDER']._serialized_start=8503
  _globals['_MARKETORDER']._serialized_end=8873
  _globals['_MARKETORDER_STATE']._serialized_start=8826
  _globals['_MARKETORDER_STATE']._serialized_end=8873
  _globals['_MARKETORDERLIST']._serialized_start=8875
  _globals['_MARKETORDERLIST']._serialized_end=8931
  _globals['_MARKETORDERPAIR']._serialized_start=8933
  _globals['_MARKETORDERPAIR']._serialized_end=8995
  _globals['_MARKETORDERPAIRLIST']._serialized_start=8997
  _globals['_MARKETORDERPAIRLIST']._serialized_end=9064
  _globals['_MARKETPRICE']._serialized_start=9066
  _globals['_MARKETPRICE']._serialized_end=9136
  _globals['_MARKETPRICELIST']._serialized_start=9138
  _globals['_MARKETPRICELIST']._serialized_end=9239
  _globals['_NULLIFIERRESULT']._serialized_start=9241
  _globals['_NULLIFIERRESULT']._serialized_end=9276
  _globals['_DECRYPTNOTESTRC20']._serialized_start=9279
  _globals['_DECRYPTNOTESTRC20']._serialized_end=9508
  _globals['_DECRYPTNOTESTRC20_NOTETX']._serialized_start=9354
  _globals['_DECRYPTNOTESTRC20_NOTETX']._serialized_end=9508
  _globals['_TRANSACTIONINFOLIST']._serialized_start=9510
  _globals['_TRANSACTIONINFOLIST']._serialized_end=9583
  _globals['_TRANSACTIONAPPROVEDLIST']._serialized_start=9586
  _globals['_TRANSACTIONAPPROVEDLIST']._serialized_end=9945
  _globals['_TRANSACTIONAPPROVEDLIST_RESULT']._serialized_start=9748
  _globals['_TRANSACTIONAPPROVEDLIST_RESULT']._serialized_end=9945
  _globals['_TRANSACTIONAPPROVEDLIST_RESULT_RESPONSE_CODE']._serialized_start=9845
  _globals['_TRANSACTIONAPPROVEDLIST_RESULT_RESPONSE_CODE']._serialized_end=9945
  _globals['_TRANSACTIONSIGNWEIGHT']._serialized_start=9948
  _globals['_TRANSACTIONSIGNWEIGHT']._serialized_end=10427
  _globals['_TRANSACTIONSIGNWEIGHT_RESULT']._serialized_start=10172
  _globals['_TRANSACTIONSIGNWEIGHT_RESULT']._serialized_end=10427
  _globals['_TRANSACTIONSIGNWEIGHT_RESULT_RESPONSE_CODE']._serialized_start=10268
  _globals['_TRANSACTIONSIGNWEIGHT_RESULT_RESPONSE_CODE']._serialized_end=10427
  _globals['_NODELIST']._serialized_start=10430
  _globals['_NODELIST']._serialized_end=10577
  _globals['_NODELIST_NODE']._serialized_start=10482
  _globals['_NODELIST_NODE']._serialized_end=10577
  _globals['_NODELIST_NODE_ADDRESS']._serialized_start=10540
  _globals['_NODELIST_NODE_ADDRESS']._serialized_end=10577
  _globals['_ACCOUNTNETMESSAGE']._serialized_start=10580
  _globals['_ACCOUNTNETMESSAGE']._serialized_end=10971
  _globals['_ACCOUNTNETMESSAGE_ASSETNETUSEDENTRY']._serialized_start=10866
  _globals['_ACCOUNTNETMESSAGE_ASSETNETUSEDENTRY']._serialized_end=10917
  _globals['_ACCOUNTNETMESSAGE_ASSETNETLIMITENTRY']._serialized_start=10919
  _globals['_ACCOUNTNETMESSAGE_ASSETNETLIMITENTRY']._serialized_end=10971
  _globals['_ACCOUNTRESOURCEMESSAGE']._serialized_start=10974
  _globals['_ACCOUNTRESOURCEMESSAGE']._serialized_end=11517
  _globals['_ACCOUNTRESOURCEMESSAGE_ASSETNETUSEDENTRY']._serialized_start=10866
  _globals['_ACCOUNTRESOURCEMESSAGE_ASSETNETUSEDENTRY']._serialized_end=10917
  _globals['_ACCOUNTRESOURCEMESSAGE_ASSETNETLIMITENTRY']._serialized_start=10919
  _globals['_ACCOUNTRESOURCEMESSAGE_ASSETNETLIMITENTRY']._serialized_end=10971
# @@protoc_insertion_point(module_scope)
