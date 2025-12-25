import argparse
from .recorder import MouseRecorder


def main(argv=None):
    parser = argparse.ArgumentParser(prog="mouse-recorder")
    parser.add_argument("--seconds", type=int, default=5, help="record duration")
    parser.add_argument("--out", type=str, default="mouse_events.json")
    args = parser.parse_args(argv)
    mr = MouseRecorder()
    mr.record_for(args.seconds)
    mr.save(args.out)
    print(f"Saved {len(mr.events)} events to {args.out}")


if __name__ == "__main__":
    main()
