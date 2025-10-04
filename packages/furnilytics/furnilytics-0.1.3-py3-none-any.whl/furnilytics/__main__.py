import argparse, json, sys, os
from .client import Client, ClientError

def main():
    p = argparse.ArgumentParser(prog="furnilytics", description="CLI for Furnilytics API (topic/subtopic/dataset)")
    p.add_argument("--api-key", default=os.getenv("FURNILYTICS_API_KEY"))
    sub = p.add_subparsers(dest="cmd", required=True)

    s_topics = sub.add_parser("topics")
    s_subt   = sub.add_parser("subtopics"); s_subt.add_argument("topic")
    s_ds     = sub.add_parser("datasets"); s_ds.add_argument("topic"); s_ds.add_argument("subtopic")
    s_flat   = sub.add_parser("list")
    s_info   = sub.add_parser("info"); s_info.add_argument("topic"); s_info.add_argument("subtopic"); s_info.add_argument("name")

    s_get    = sub.add_parser("get");  s_get.add_argument("topic"); s_get.add_argument("subtopic"); s_get.add_argument("name")
    s_get.add_argument("--limit", type=int, default=None, help="If omitted, fetches ALL rows with auto-pagination")
    s_get.add_argument("--offset", type=int, default=0)
    s_get.add_argument("--select")
    s_get.add_argument("--order_by"); s_get.add_argument("--order_dir")
    s_get.add_argument("--frm"); s_get.add_argument("--to")
    s_get.add_argument("--filters", help='JSON dict of filters, e.g. {"country":"SE"}')
    s_get.add_argument("--kv", nargs="*", help="Extra key=value pairs (column filters)")
    s_get.add_argument("--page-size", type=int, default=1000, help="Chunk size when auto-paginating (default 1000)")
    s_get.add_argument("--max-rows", type=int, default=None, help="Safety cap when fetching all")
    s_get.add_argument("--csv", help="Write result to CSV file")

    args = p.parse_args()
    if not args.api_key:
        print("Error: missing API key. Pass --api-key or set FURNILYTICS_API_KEY.", file=sys.stderr)
        sys.exit(1)

    cli = Client(api_key=args.api_key)
    try:
        if args.cmd == "topics":
            df = cli.list_topics(); print(df.to_string(index=False))
        elif args.cmd == "subtopics":
            df = cli.list_subtopics(args.topic); print(df.to_string(index=False))
        elif args.cmd == "datasets":
            df = cli.list_datasets(args.topic, args.subtopic); print(df.to_string(index=False))
        elif args.cmd == "list":
            df = cli.list_datasets_flat(); print(df.to_string(index=False))
        elif args.cmd == "info":
            meta_df, columns_df = cli.dataset_info(args.topic, args.subtopic, args.name)
            print("Meta:"); print(meta_df.to_string(index=False))
            print("\nColumns:"); print(columns_df.to_string(index=False))
        elif args.cmd == "get":
            params = {
                "limit": args.limit,
                "offset": args.offset,
                "page_size": args.page_size,
                "max_rows": args.max_rows
            }
            if args.select: params["select"] = args.select.split(",")
            for k in ["order_by","order_dir","frm","to"]:
                v = getattr(args, k)
                if v is not None: params[k]=v
            if args.filters:
                try: params["filters"] = json.loads(args.filters)
                except Exception: raise SystemExit("Invalid JSON for --filters")
            if args.kv:
                for kv in args.kv:
                    if "=" in kv:
                        k,v = kv.split("=",1)
                        params.setdefault("filters", {})
                        if isinstance(params["filters"], dict): params["filters"][k]=v

            df = cli.get(args.topic, args.subtopic, args.name, **params)
            if args.csv:
                df.to_csv(args.csv, index=False)
                print(f"Wrote {len(df)} rows to {args.csv}")
            else:
                print(df.to_string(index=False))
        else:
            p.error("Unknown command")
    except ClientError as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)

if __name__ == "__main__":
    main()
