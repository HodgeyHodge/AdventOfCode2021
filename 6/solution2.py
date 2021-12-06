
# a more cunning way: one fish at a time, and breaking up the length of time

def dictify_fish_list(fish_list):
    fish_dict = {}
    for fish in fish_list:
        if fish in fish_dict:
            fish_dict[fish] += 1
        else:
            fish_dict[fish] = 1
    return fish_dict
    
def iterate_list(fish_list):
    new_list = []
    for fish in fish_list:
        if fish > 0:
            new_list.append(fish - 1)
        elif fish == 0:
            new_list.append(6)
            new_list.append(8)
    return new_list

def iterate_list_repeatedly(fish_list, days):
    for i in range(0, days):
        fish_list = iterate_list(fish_list)
    return dictify_fish_list(fish_list)


def fish_fecundity_stats_at_x_days(days):
    return {
        0: (iterate_list_repeatedly([0], days)),
        1: (iterate_list_repeatedly([1], days)),
        2: (iterate_list_repeatedly([2], days)),
        3: (iterate_list_repeatedly([3], days)),
        4: (iterate_list_repeatedly([4], days)),
        5: (iterate_list_repeatedly([5], days)),
        6: (iterate_list_repeatedly([6], days)),
        7: (iterate_list_repeatedly([7], days)),
        8: (iterate_list_repeatedly([8], days))
    }

filename = "input.txt"

with open(filename) as file:
    fish_list = [int(i) for i in file.readline().split(',')]
    fish_dict_at_0_days = dictify_fish_list(fish_list)

# with our intial fish population, can calculate population after 128 days, fishwise:

fish_fecundity_stats_at_128_days = fish_fecundity_stats_at_x_days(128)

fish_dict_at_128_days = {}
for age_cohort in fish_dict_at_0_days:
    for descendents in fish_fecundity_stats_at_128_days:
        if descendents not in fish_dict_at_128_days:
            fish_dict_at_128_days[descendents] = fish_dict_at_0_days[age_cohort] * fish_fecundity_stats_at_128_days[age_cohort][descendents]
        else:
            fish_dict_at_128_days[descendents] += fish_dict_at_0_days[age_cohort] * fish_fecundity_stats_at_128_days[age_cohort][descendents]
    print(fish_dict_at_128_days)

# then calculate the number at 256 days by the same arithmetic on the new starting population:

fish_dict_at_256_days = {}
for age_cohort in fish_dict_at_128_days:
    for descendents in fish_fecundity_stats_at_128_days:
        if descendents not in fish_dict_at_256_days:
            fish_dict_at_256_days[descendents] = fish_dict_at_128_days[age_cohort] * fish_fecundity_stats_at_128_days[age_cohort][descendents]
        else:
            fish_dict_at_256_days[descendents] += fish_dict_at_128_days[age_cohort] * fish_fecundity_stats_at_128_days[age_cohort][descendents]
    print(fish_dict_at_256_days)

