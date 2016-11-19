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
                     default='./bmode_ultrasound/rfdat.bin')

    par.add_argument("--m",
                     dest="m",
                     help="JSON Metadata File Name",
                     default='./bmode_ultrasound/bmode.json')

    par.add_argument("--display",
                     dest="d",
                     help="Display Generated Image <True/False>",
                     type=bool,
                     default=False)

    par.add_argument("--save",
                     dest="s",
                     help="Save Output Image <True/False>",
                     type=bool,
                     default=True)

    par.add_argument("--out",
                     dest="out",
                     help="Output Filename for Generated Image",
                     default="./outputs/bmode.png")

    par.add_argument("--dr",
                     dest="dr",
                     help="Lower Bound of Dynamic range",
                     type=float,
                     default=-50.)

    par.add_argument("--heq",
                     dest="heq",
                     help="Enable Adaptive Histogram Equalization "
                          "<True/False>",
                     type=bool,
                     default=False)

    par.add_argument("--post",
                     dest="post",
                     help="Apply Image Post Processing <True/False>",
                     type=bool,
                     default=False)

    par.add_argument("--units",
                     dest="u",
                     help="Units for display <mm, cm, m>",
                     default='cm')

    par.add_argument("--log",
                     dest="l",
                     help="Logging Level <DEBUG, INFO, WARNING, ERROR>",
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

    return args
