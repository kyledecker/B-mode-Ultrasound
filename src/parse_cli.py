def parse_cli():

    """parse CLI

    :returns: args
    """
    import argparse as ap

    par = ap.ArgumentParser(description="US Image Formation From Raw RF Data",
                            formatter_class=ap.ArgumentDefaultsHelpFormatter)

    par.add_argument("--f",
                     dest="f",
                     help="RF Binary Data File Name",
                     default='rfdat.bin')

    par.add_argument("--m",
                     dest="m",
                     help="JSON Metadata File Name",
                     default='bmode.json')

    par.add_argument("--display",
                     dest="d",
                     help="Display Generated Image",
                     type=bool,
                     default=False)

    par.add_argument("--save",
                     dest="s",
                     help="Save Output Image",
                     type=bool,
                     default=True)

    par.add_argument("--out",
                     dest="out",
                     help="Output Filename for Generated Image",
                     default="bmode.png")

    par.add_argument("--log",
                     dest="l",
                     help="Logging Level",
                     default='DEBUG')

    par.add_argument("--shoutout",
                     dest="shoutout",
                     help="shoutout message",
                     default="Ultrasound Image Formation From Raw RF Data")

    par.add_argument("--noshoutout",
                     dest="noshoutout",
                     help="suppress shoutout message printing",
                     action="store_true")

    args = par.parse_args()

    return(args)
