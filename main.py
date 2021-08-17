#pip3 install absl-py

from absl import app, flags
FLAGS = flags.FLAGS

flags.DEFINE_string("instance", None, help="Path to the instance file")
flags.DEFINE_integer("N", 0, help="Clients number of instance")
flags.DEFINE_boolean("toy", False, 'Boolean flag.')
#flags.DEFINE_boolean("debug", True, 'Boolean flag.')
#flags.DEFINE_boolean("debug_level2", False, 'Boolean flag.')


from vrp import VRPTW, solomon, example


def main(argv):

    if FLAGS.toy:
        vrptw = example.create_renatos_example()
        vrptw.print_instance()
        solomon.insertion_heuristic(vrptw, alpha1=0.5, alpha2=0.5, mu=1, lambdaa=1, debug=True, debug_level2=True)
    else:
        if FLAGS.instance is not None:
            vrptw = VRPTW(FLAGS.N +1) #depot
            vrptw.read_instance(FLAGS.instance)
        else:
            print("Please describe the instace file.\nAborting...")
            exit(1)
        vrptw.print_instance()
        solomon.insertion_heuristic(vrptw, alpha1=0.5, alpha2=0.5, mu=1, lambdaa=1, debug=False, debug_level2=False)
    
    

if __name__ == "__main__":
    app.run(main)
