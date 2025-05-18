import statistics

def compute_statistics(nums):
    stats = {"середнє": statistics.mean(nums), "медіана": statistics.median(nums)}

    try:
        stats["мода"] = statistics.mode(nums)
    except statistics.StatisticsError:
        stats["мода"] = "немає моди"

    return stats
