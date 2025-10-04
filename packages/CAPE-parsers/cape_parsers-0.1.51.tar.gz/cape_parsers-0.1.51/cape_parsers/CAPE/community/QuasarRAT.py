from rat_king_parser.rkp import RATConfigParser


def extract_config(data: bytes):
    return RATConfigParser(data=data).report.get("config", {})
