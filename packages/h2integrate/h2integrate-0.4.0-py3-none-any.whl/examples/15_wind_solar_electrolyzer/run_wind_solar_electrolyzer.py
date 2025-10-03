from h2integrate.core.h2integrate_model import H2IntegrateModel


# Create a H2Integrate model
model = H2IntegrateModel("15_wind_solar_electrolyzer.yaml")

# Run the model
model.run()

model.post_process()
