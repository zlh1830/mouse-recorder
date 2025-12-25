from mouse_recorder.recorder import MouseRecorder
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=5, help="record duration")
    parser.add_argument("--out", type=str, default="mouse_events.json")
    args = parser.parse_args()
    mr = MouseRecorder()
    mr.record_for(args.seconds)
    mr.save(args.out)
    print(f"Saved {len(mr.events)} events to {args.out}")


if __name__ == "__main__":
    main()
