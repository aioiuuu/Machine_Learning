from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter(log_dir="../src/logs")
for step in range(100):
    writer.add_scalar("scaler/y=x",step,step)
    writer.add_scalar("scaler/y=x^2",step*step,step)
writer.close()