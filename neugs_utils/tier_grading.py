from typing import Dict, List
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

## common TIER 

COMMON_ONE = "learning"
COMMON_TWO = "approaching"
COMMON_THREE = "meets"
COMMON_FOUR = "exceeds"

class tier(object):
    """An wrapper that modifies the tags attribute to include a dictionary specifying the tier
    """
    def __init__(self, val : str):
        self.tier = val


    def __call__(self, func):
        if hasattr(func, "__tags__") :
            func.__tags__ = {"tier": self.tier, "tags": func.__tags__}
        else:
            func.__tags__ = {"tier" : self.tier}
        return func



class TierMasteryJSONTestRunner(JSONTestRunner):
    failed = None

    def __init__(self, tiers=(COMMON_ONE, COMMON_TWO, COMMON_THREE, COMMON_FOUR), score_per_tier = 1, stop_grading=True, **kargs):
        self.tiers = tiers
        self.stop_grading = stop_grading
        self.score_per_tier = score_per_tier
        if 'post_processor' in kargs:
            self.second_processor = kargs['post_processor']
            del kargs['post_processor']
        else:
            self.second_processor = lambda a : a ## a do nothing function
        super().__init__(post_processor=self.post_processor, **kargs)


    def post_processor(self, json: Dict) -> Dict:
        """A post-processing wrapper for gradescope_utils.autograder_utils.json_test_runner.JSONTestRunner. The wrapper
        will either use the default config file, or a config file set before the post processor call 

        Args:
            json (Dict): json graded test result generated by JSONTestRunner

        Returns:
            Dict: A new modified dict for printing out
        """
        json["score"] = sum((self.__check_tests(self._filter(json['tests'], tier), tier)   for tier in self.tiers))
        return self.second_processor(json)

    def _filter(self, tests: List, tier: str) -> List:
        """Helper method to filter a group of tests based on the tier (due to complexity of the if statement)

        Args:
            json (Dict): the results dictionary being processed

        Returns:
            List: the tests that match the filter based on the tier 
        """
        return [x for x in tests if ("tags" in x) and ("tier" in x["tags"]) and (x['tags']['tier'] == tier)]


    def __check_tests(self, tests: List, tier: str) -> int:
        """Loops through all the tests for the tier. If the previous tier has
        already failed, then cleans up the info for that tier

        Args:
            tests (List): a list of tests to check
            tier (str): the tier mainly used for setting the self.failed and the common update on test names

        Returns:
            int: the score 1 if all tests passed, or 0 if *any* test failed
        """
        if len(tests) < 1 : return 0 # don't score empty tiers
        score = self.score_per_tier
        if self.failed is not None and self.stop_grading: 
            self.__remove_tier(tests)
            score = 0
        fail_count = sum((1 for test in tests if test["status"] == "failed"))         
        if fail_count > 0:
            self.failed = tier
            score = 0
        self.__common_update(tests, tier)
        return score 

    def __common_update(self, tests: List, tier: str) -> None:
        """Updating the autograder tags to better match Mastery Tier based grading. 
        Assumed a tier for them to be grouped by

        Args:
            tests (List): The tests to update
            tier (str): the tier they are all associated with
        """
        for test in tests:
            if "score" in test:
                del test["score"] #not needed as there will be one at the top level
            test["name"] = f"{tier.capitalize()}: {test['name']}"
            
            if "tags" in test["tags"]:
                test["tags"] = tuple(test["tags"]["tags"]) 
            else:
                # remove the tag used for the tier
                del test["tags"]


    def __remove_tier(self, tests: List) -> None:
        """
        Removes the test results from that tier, even they have been completed. Often
        called after one tier has failed already.

        Args:
            tests (List): A group of tests to remove results from, and mark all as failed.
        """
        for test in tests:
           test["status"] = "failed"
           test["output"] = f"Test Skipped: {str(self.failed).capitalize()} Tier needs corrected and resubmitted first"