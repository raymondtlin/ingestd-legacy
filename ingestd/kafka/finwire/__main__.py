import argparse


def main(args):

    if args.mode == "produce":
        produce(args.topic, conf)
    else:
        # Fallback to earliest to ensure all messages are consumed
        conf['group.id'] = args.group
        conf['auto.offset.reset'] = "earliest"
        consume(args.topic, conf)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Example client for handling Avro data")
    parser.add_argument('-t', dest="topic", default="example_avro",
                        help="Topic name")
    parser.add_argument('mode', choices=['produce', 'consume'],
                        help="Produce or Consume messages")
    parser.add_argument('-g', dest="group", default="example_avro",
                        help="Consumer group; required if running 'consumer' mode")

main(parser.parse_args())