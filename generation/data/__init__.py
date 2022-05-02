from .datasets import  Dataset
from torch.utils.data import DataLoader

def get_loader(args):
    # datasets
    dataset = Dataset(root=args.root1, batch_size=args.batch_size, crop_size=args.crop_size)
    dataset2 = Dataset(root=args.root2, batch_size=args.batch_size, crop_size=args.crop_size)

    # loaders
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False, num_workers=0)
    loader2 = DataLoader(dataset2, batch_size=args.batch_size, shuffle=False, num_workers=0)
    return loader, loader2
