import matplotlib.pyplot as plt # type: ignore

class Plotter:
    @staticmethod
    def plot(parent_frame, plot_type, month):
        fig, ax = plt.subplots()
        if plot_type == 2:
            # Generate protocol plot
            ax.set_title("Protocol Plot")
        elif plot_type == 3:
            # Generate month plot
            ax.set_title("Month Plot")

        plt.show()