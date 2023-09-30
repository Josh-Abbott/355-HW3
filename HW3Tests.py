#------------------------------------------------------
#-- INCLUDE YOUR OWN TESTS IN THIS FILE
#------------------------------------------------------
import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        pass

    def sort_values(self,d):
        return dict(map(lambda t: (t[0],list(sorted(t[1]))), d.items()))
    
    #--- Problem 1(a)----------------------------------
    
    def test_aggregate_log(self):
        pass
        # Provide your own test here. Create your own input dictionary for this test.
        log_input = {'MATH273':{'Fri':8,'Mon':3,'Sun':5},
                     'MATH220':{'Tue':4,'Wed':1,'Thu':5, 'Fri':1},
                     'PHYSICS202':{'Mon':4,'Wed':2,'Sat':6},
                     'CptS317':{'Wed':3,'Tue':7,'Fri':2,'Sat':3},
                     'PHYSICS212':{'Sun':3,'Wed':3}}
        
        output = {'Fri': 11, 'Mon': 7, 'Sun': 8, 'Tue': 11, 'Wed': 9, 'Thu': 5, 'Sat': 9}
        self.assertDictEqual(aggregate_log(log_input),output)
    
    #--- Problem 1(b)----------------------------------
    def test_combine_dict(self):
        pass
        # Provide your own test here. Create your own input dictionary for this test .
        # You can re-use the data dictionary you created for problem-1.
        log1 = {'Fri':8,'Mon':3,'Sun':5}
        log2 = {'Mon':4,'Wed':2,'Sat':6}
        output = {'Fri': 8, 'Mon': 7, 'Sun': 5, 'Wed': 2, 'Sat': 6}
        self.assertDictEqual(combine_dict(log1,log2),output)
        #make sure input dictionaries are not changed. 
        self.assertDictEqual(log1, {'Fri':8,'Mon':3,'Sun':5})
        self.assertDictEqual(log2, {'Mon':4,'Wed':2,'Sat':6})

    #--- Problem 1(c) ----------------------------------
    def test_merge_logs(self):
        pass
        # Provide your own test here. Create your own input dictionary for this test .
        # You can re-use the data dictionary you created for problem-1.
        log_list_backup = [{'MATH273':{'Fri':8,'Mon':3,'Sun':5},'MATH220':{'Tue':4,'Wed':1,'Thu':5, 'Fri':1},'PHYSICS202':{'Mon':4,'Wed':2,'Sat':6},'CptS317':{'Wed':3,'Tue':7,'Fri':2,'Sat':3},'PHYSICS212':{'Sun':3,'Wed':3}},
             {'MATH220':{'Wed':4, 'Mon':5},'PHYSICS202':{'Sun':2, 'Fri':3, 'Tue':1},'CptS317':{'Thu':7}},
             {'PHYSICS202':{'Sat':7},'PHYSICS212':{'Fri':5,'Thu':6},'MATH273':{'Tue':5,'Mon':2,'Sat':2},'MATH220':{'Mon':1,'Sun':8}}]
        log_list = [{'MATH273':{'Fri':8,'Mon':3,'Sun':5},'MATH220':{'Tue':4,'Wed':1,'Thu':5, 'Fri':1},'PHYSICS202':{'Mon':4,'Wed':2,'Sat':6},'CptS317':{'Wed':3,'Tue':7,'Fri':2,'Sat':3},'PHYSICS212':{'Sun':3,'Wed':3}},
             {'MATH220':{'Wed':4, 'Mon':5},'PHYSICS202':{'Sun':2, 'Fri':3, 'Tue':1},'CptS317':{'Thu':7}},
             {'PHYSICS202':{'Sat':7},'PHYSICS212':{'Fri':5,'Thu':6},'MATH273':{'Tue':5,'Mon':2,'Sat':2},'MATH220':{'Mon':1,'Sun':8}}]
        
        output = {'MATH273': {'Fri': 8, 'Mon': 5, 'Sun': 5, 'Tue': 5, 'Sat': 2}, 'MATH220': {'Tue': 4, 'Wed': 5, 'Thu': 5, 'Fri': 1, 'Wed': 5, 'Mon': 6, 'Sun': 8}, 'PHYSICS202': {'Mon': 4, 'Wed': 2, 'Sat': 13, 'Sun': 2, 'Fri': 3, 'Tue': 1}, 'CptS317': {'Wed': 3, 'Tue': 7, 'Fri': 2, 'Sat': 3, 'Thu': 7}, 'PHYSICS212': {'Sun': 3, 'Wed': 3, 'Fri': 5, 'Thu': 6}}
        self.assertDictEqual(self.sort_values(merge_logs(log_list)),self.sort_values(output))
        self.assertListEqual(log_list,log_list_backup)

    #--- Problem 2(a)----------------------------------
    def test_most_hours(self):
        pass
        # Provide your own test here. Create your own input dictionary for this test 
        self.log_input = {'MATH273':{'Fri':8,'Mon':3,'Sun':5},
                     'MATH220':{'Tue':4,'Wed':1,'Thu':5, 'Fri':1},
                     'PHYSICS202':{'Mon':4,'Wed':2,'Sat':6},
                     'CptS317':{'Wed':3,'Tue':7,'Fri':2,'Sat':3},
                     'PHYSICS212':{'Sun':3,'Wed':3}}
        
        output = ('MATH273', 16)
        self.assertTupleEqual(most_hours(self.log_input),output)

            
    #--- Problem 2(b) ----------------------------------
    def test_filter_log(self):
        pass
        # Provide your own test here. Create your own input dictionary for this test 
        self.log_input = {'MATH273':{'Fri':8,'Mon':3,'Sun':5},
                     'MATH220':{'Tue':4,'Wed':1,'Thu':5, 'Fri':1},
                     'PHYSICS202':{'Mon':4,'Wed':2,'Sat':6},
                     'CptS317':{'Wed':3,'Tue':7,'Fri':2,'Sat':3},
                     'PHYSICS212':{'Sun':3,'Wed':3}}
        
        output = sorted(['CptS317', 'PHYSICS202', 'PHYSICS212'])
        self.assertListEqual(sorted(filter_log(self.log_input,"Wed", 2)),output)

    #--- Problem 3----------------------------------
    def test_graph_cycle(self):
        pass
        # Provide your own test here.   Create your own input graph for this test 
        self.graph = {'F':('G',3),'K':('E',6),'Q':('T',4),'O':('P',3),'A':('B',3),'E':('V',8),'P':('R',8),'R':('K',4),'V':('P',9)} # need to change
        
        output = ['P', 'R', 'K', 'E', 'V', 'P']
        self.assertListEqual(graph_cycle(self.graph,'O'),output)


    #--- Problem 4----------------------------------
    def test_filter_iter(self):
        pass
        # Provide your own test here. Initialize the iterator with your own input.
        it = iter([5,9,3,10,6,8,2,-4,-8,3,6,-11,-2,1,-1,6,-8,-4,7])
        expected_output = [3,2,-4,-8,3,-11,-2,1,-1,-8,-4]
        actual_output = list(filter_iter(it, lambda x: x*2<10))  #convert the iterator output to list
        self.assertListEqual(actual_output, expected_output)

    #--- Problem 5----------------------------------
    def test_merge(self):
        pass
        # Provide your own test here.
        it1 = filter_iter(iter([2,7,3,6,9,-4,5,7,9,-3,4,8,4,7,-5,-8,3,5]), lambda x: x>2)
        it2 = filter_iter(iter([5,8,3,3,-3,-7,8,4,7,2,6,-4,-1,1,8,9,3,2,7,5,-3,4,-2,1,9]), lambda x: x%2==0)
        
        self.assertListEqual(merge(it1,it2, 11), [7,3,6,8,8,4,2,6,-4,8,2])
        self.assertListEqual(merge(it1,it2, 8), [-2,5])
        self.assertListEqual(merge(it1,it2, 5), [])


if __name__ == '__main__':
    unittest.main()

