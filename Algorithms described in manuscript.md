# Algorithms

This document contains the algorithms presented in the manuscript
"Web Application Security Testing Using Misuse Case Based Test Model."

---

## Algorithm 1: Test Model Graph Generation from misuse case specifications



Input:  Misuse Case Specification (MCS)
Output: Test Model Graph TMG = (V, E)
Begin:   Initialize: V ← ∅, E ← ∅
  For each step BSi in BTF do
        Create node(BSi)
        V ← V ∪ {BSi}
        If BSi is not the first step then
              E ← E ∪ {(previous(BSi), BSi)}
        End If
        If BSi = "FOREACH" then
              Let LoopStart ← BSi
        End If
        If BSi = "ENDFOR" then
              E ← E ∪ {(BSi, LoopStart)}
              Let ExitStep ← next(BSi)
              E ← E ∪ {(LoopStart, ExitStep)}
        End If
  End For
  For each SATFj do
        Let RFSj ← Resume Flow Step of SATFj
        E ← E ∪ {(RFSj, first(SATFj))}
        For each step TSi in SATFj do
              Create node(TSi)
              V ← V ∪ {TSi}
              If TSi is not the first step then
                    E ← E ∪ {(previous(TSi), TSi)}
              End If
        End For
        Let ResumeTarget ← ResumeTarget(SATFj)
        E ← E ∪ {(last(SATFj), ResumeTarget)}
  End For
  For each SAFk do
        Let BSx ← linked Basic Flow Step of SAFk
        E ← E ∪ {(BSx, first(SAFk))}
        For each step SFi in SAFk do
              Create node(SFi)
              V ← V ∪ {SFi}
              If SFi is not the first step then
                    E ← E ∪ {(previous(SFi), SFi)}
              End If
        End For
        Create node(ACCESS DENIED,_k)
        V ← V ∪ {ACCESS DENIED_k}
        E ← E ∪ {(last(SAFk), ACCESS DENIED_k)}
  End For
  Create node(POSTCONDITION_SUCCESS)
  V ← V ∪ {POSTCONDITION_SUCCESS}
  If last(BTF) = "ENDFOR" then
        E ← E ∪ {(previous(last(BTF)), POSTCONDITION_SUCCESS)}
  Else
        E ← E ∪ {(last(BTF), POSTCONDITION_SUCCESS)}
  End If
  Return TMG = (V, E)
End.


## Algorithm 2. Test Sequence Generation from Test Model Graph


Input: Test Model Graph (TMG), Start Node (SN), End Nodes (EN) = {Access Denied, Postcondition Success, Terminate}
Output: Test Sequences (TS)
function test_seq_generation(TMG, SN, EN)
      TS ← ∅
      LoopCounter ← empty_map
      function dfstraversal(current_node, current_testpath, Loopcounter_copy)
            append(current_testpath, current_node)
            If (current_node ∈ EN) then
                  TS ← TS ∪ {copy(current_testpath)}
            Else
                  For each neighbor_node ∈
                        getNeighbors_nodes(TMG, current_node) do
                        If (isLoopEdge(current_node, neighbor_node)) then
      If (Loopcounter_copy[(current_node, neighbor_node)] < 1) then
            Loopcounter_copy[(current_node, neighbor_node)] ← 0 + 1
            dfstraversal(neighbor_node, current_testpath, Loopcounter_copy)
      End If
Else If (neighbor_node ∉ current_testpath) then
      dfstraversal(neighbor_node, current_testpath, Loopcounter_copy)
End If                
  End For
            End If
            removelast(current_testpath)
      End dfstraversal
      dfstraversal(SN, empty_list, copy (Loopcounter))
      Return TS
End test_seq_generation


## Algorithm 3. Pseudo-code to generate OCL Constraints



Inputs: Class model (class, methods), Cause-effect Rule
Output: Set of OCL constraints.
1.	function Generate_constraint(class model, cause effect rule)
2.	Constraint-setΦ
3.	Foreach Cause-Effect Rules:  
a.	Capture Cause and effect
b.	Parse CAUSE into:  
i.	Object Instance (o)
ii.	VARIABLE (Class Method or Association)  
iii.	OPERATOR (=) 
iv.	RHS (true | false)  
4.	OCL_constraint constraint using constraint pattern grammar
5.	Constraint-set  OCL_constraint ∪ constraint-set
 End for
6.	Return Constraint_set  
End function.

