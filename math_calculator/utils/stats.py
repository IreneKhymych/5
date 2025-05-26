import statistics

def compute_statistics(nums):
    stats = {"середнє": statistics.mean(nums), "медіана": statistics.median(nums)}
    modes = statistics.multimode(nums)
    stats["мода"] = modes[0] if len(modes) == 1 else "немає моди"
    return stats
