"""
    This file includes example (description, model) pairs used for few-shots learning. Some process description are
    from the PET data set "Patrizio Bellan, Han van der Aa, Mauro Dragoni, Chiara Ghidini, and Simone Paolo Ponzetto.
    PET: an annotated dataset for process extraction from natural language text tasks. In Business Process Management
    Workshops 2022, Revised Selected Papers, volume 460 of Lecture Notes in Business Information Processing,
    pages 315–321. Springer, 2022".
"""


from promoai.model_generation import ModelGenerator

d1 = (
    "in this process, you can either do 'a' or 'b'. If 'a' is selected,"
    " then it can be repeated. After completing 'a' or 'b', 'c' may be executed. c is always followed by 'd'."
    " Finally another"
    " execution of 'a' is performed. The whole process is optional and can be skipped."
)


def m1():
    gen = ModelGenerator()
    a = gen.activity("a")
    a_copy = gen.copy(a)
    a_looped = gen.self_loop(a)
    b = gen.activity("b")
    c = gen.activity("c")
    d = gen.activity("d")
    seq_c_d = gen.partial_order(dependencies=[(c, d)])
    skippable_c_d = gen.skip(seq_c_d)
    dg = gen.decision_graph(dependencies=[
        (None, a_looped),
        (None, b),
        (a_looped, skippable_c_d),
        (b, skippable_c_d),
        (skippable_c_d, a_copy),
        (a_copy, None),
    ])
    final_model = gen.skip(dg)
    return final_model


e1 = (
    "a common error for this process is to add a dependency 'd -> a' without creating a"
    " copy of 'a'. This would imply that the whole process can be executed once again, which is not stated in the description."
    " Another common error is not to mark the sequence c -> d as skippable."
)

d1_2 = (
    "in this process, you can either do 'a' or 'b'. If 'a' is selected,"
    " then it can be repeated. After completing 'a' or 'b', 'c' is executed, followed by 'd'. Finally, the process"
    " either ends or goes back to 'a'."
)


def m1_2():
    gen = ModelGenerator()
    a = gen.activity("a")
    a_looped = gen.self_loop(a)
    b = gen.activity("b")
    c = gen.activity("c")
    d = gen.activity("d")
    final_model = gen.decision_graph(dependencies=[
        (None, a_looped),
        (None, b),
        (a_looped, c),
        (b, c),
        (c, d),
        (d, a_looped),
        (d, None)
    ])
    return final_model


e1_2 = (
    "A common error for this process is to create a copy of 'a' instead of looping back. Another "
    "common mistake here would be to break the process into separable parts, e.g., partial order expressing (c,d)."
    "This is not necessary, as decision graphs can express simple sequential dependencies."
)

d2 = (
    "inventory management can proceed through restocking items or fulfilling orders. Restocking can be performed as "
    "often as necessary. Following either restocking or order fulfillment, an inventory audit is carried out. If"
    " unexpected behavior is detected in the inventory audit, then a data analysis is performed."
    " Additionally, urgent restocking needs can bypass regular restocking and "
    "order fulfillment processes directly leading to the inventory audit. This entire process is modular and can be "
    "repeated or skipped based on operational requirements."
)


def m2():
    gen = ModelGenerator()
    restock = gen.self_loop(gen.activity("restock items"))
    fulfil = gen.activity("fulfill orders")
    urgent_restock = gen.activity("urgent restock")
    inventory_audit = gen.activity("inventory audit")
    data_analysis = gen.activity("data analysis")
    dg = gen.decision_graph(dependencies=[
        (None, restock),
        (None, fulfil),
        (None, urgent_restock),
        (restock, inventory_audit),
        (fulfil, inventory_audit),
        (urgent_restock, inventory_audit),
        (inventory_audit, data_analysis),
        (inventory_audit, None),
        (data_analysis, None)
    ])
    final_model = gen.skip(gen.self_loop(dg))
    return final_model


e2 = "a common error for this process is to copy 'inventory_audit'. Another common error is to create a partial order for" \
" sequential dependencies that can be expressed via the decision graph. Additionally, a common mistake is to omit the self-loop on 'restock items' or on the whole process."

d3 = (
    "This enhanced payroll process allows for a high degree of customization and adaptation to specific "
    "requirements. Employees' time can be tracked with the option to repeat this step as needed. Pay calculations "
    "follows, incorporating diverse factors such as overtime, bonuses, and deductions. Subsequently, the process "
    "facilitates the issuance of payments and the generation of detailed reports. "
)


def m3():
    gen = ModelGenerator()
    track_time = gen.activity("track time")
    track_time_looped = gen.self_loop(track_time)
    activity_2 = gen.activity("calculate pay")
    activity_3 = gen.activity("issue payments")
    activity_4 = gen.activity("generate reports")
    final_model = gen.partial_order(
        dependencies=[
            (track_time_looped, activity_2),
            (activity_2, activity_3),
            (activity_2, activity_4),
        ]
    )
    return final_model


e3 = (
    "a common error for this process is to model a choice between activity_3 and activity_4 instead of the"
    " concurrency. Additionally, a common mistake is to try to model the final model as a decision graph instead"
    " of a partial order. This is not possible here, as decision graphs cannot express the concurrency between"
    " activity_3 and activity_4."
)

d4 = (
    "This system combines 4 parallel subprocesses, i.e., that are executed independently/at the same time. The first "
    "process starts with A followed by B then a choice of C and D. The second process consists of a single activity "
    "E which can be repeated but must be executed at least once. The third process consists of the activity F, "
    "which can be repeated or skipped. The last process contains the parallel activities G, H, I, J with the "
    "constrains that I must precede J and H must precede I "
)


def m4():
    gen = ModelGenerator()

    # subprocess 1
    a = gen.activity("a")
    b = gen.activity("b")
    c = gen.activity("c")
    d = gen.activity("d")
    choice_c_d = gen.decision_graph(dependencies=[(None, c), (None, d), (c, None), (d, None)])

    # subprocess 2
    e = gen.activity("e")   
    unskippable_self_loop_e = gen.self_loop(e)

    # subprocess 3
    f = gen.activity("f")
    skippable_self_loop_f = gen.skip(gen.self_loop(f))

    # subprocess 4
    g = gen.activity("g")
    h = gen.activity("h")
    i = gen.activity("i")
    j = gen.activity("j")

    # combine all subprocesses
    final_model = gen.partial_order(
        dependencies=[
            (a, b),
            (b, choice_c_d),
            (unskippable_self_loop_e,),
            (skippable_self_loop_f,),
            (g,),
            (h, i),
            (i, j),
        ]
    )
    return final_model


e4 = (
    "a common error for this process is to create partial orders for some subprocesses, then trying to add a"
    " partial order as a child of another partial order. Note that the behavior cannot be expressed with one decision graph"
    " because decision graphs cannot express concurrency."
)

d5 = (
    "A customer brings in a defective computer and the CRS checks the defect and hands out a repair cost calculation "
    "back. If the customer decides that the costs are acceptable , the process continues , otherwise she takes her "
    "computer home unrepaired. The ongoing repair consists of two activities , which are executed , in an arbitrary "
    "order. The first activity is to check and repair the hardware , whereas the second activity checks and "
    "configures the software. After each of these activities , the proper system functionality is tested. If an "
    "error is detected another arbitrary repair activity is executed , otherwise the repair is finished. "
)


def m5():
    gen = ModelGenerator()
    defect_check = gen.activity("Check defect")
    cost_calculation = gen.activity("Calculate repair costs")
    cancel = gen.activity("Cancel and give computer unrepaired")
    repair_hardware = gen.activity("Check and repair the hardware")
    repair_software = gen.activity("Check and configure the software")
    test_functionality_after_hardware_repair = gen.activity("Test system functionality")
    test_functionality_after_software_repair = gen.activity("Test system functionality")
    additional_hardware_repair = gen.activity("Perform additional hardware repairs")
    skippable_repair_after_hardware_repair = gen.skip(additional_hardware_repair)
    additional_software_repair = gen.activity("Perform additional software repairs")
    skippable_repair_after_software_repair = gen.skip(additional_software_repair)
    finish_repair = gen.activity("Finish repair")
    partial_order_repairs = gen.partial_order(
        dependencies=[(repair_hardware, test_functionality_after_hardware_repair), (repair_software, test_functionality_after_software_repair),
                      (test_functionality_after_hardware_repair, skippable_repair_after_hardware_repair),
                      (test_functionality_after_software_repair, skippable_repair_after_software_repair)]
    )
    final_model = gen.decision_graph(dependencies=[
        (None, defect_check),
        (defect_check, cost_calculation),
        (cost_calculation, cancel),
        (cancel, None),
        (cost_calculation, partial_order_repairs),
        (partial_order_repairs, finish_repair),
        (finish_repair, None),
    ])


    return final_model


e5 = (
    "a common error for this process is to create partial orders for some subprocesses, then trying to add a"
    " partial order as a child of another partial order. Another very important error you should avoid is to"
    " create a local choice between 'cancel' and some local activity (e.g., 'continue process') instead of"
    " modeling a choice between 'cancel' and the rest of the process. Additionally, a common mistake is to integrate the partial order into the decision graph."
)

d6 = (
    "A small company manufactures customized bicycles. Whenever the sales department receives an order , "
    "a new process instance is created. A member of the sales department can then reject or accept the order "
    "for a customized bike. In the former case , the process instance is finished. In the latter case , "
    "the storehouse and the engineering department are informed. The storehouse immediately processes the part "
    "list of the order and checks the required quantity of each part. If the part is available in-house , "
    "it is reserved. If it is not available , it is back-ordered. This procedure is repeated for each item on "
    "the part list. In the meantime, the engineering department prepares everything for the assembling of the "
    "ordered bicycle. If the storehouse has successfully reserved or back-ordered every item of the part list "
    "and the preparation activity has finished, the engineering department assembles the bicycle. Afterwards "
    ", the sales department ships the bicycle to the customer and finishes the process instance . "
)


def m6():
    gen = ModelGenerator()
    create_process = gen.activity("Create process instance")
    reject_order = gen.activity("Reject order")
    accept_order = gen.activity("Accept order")
    inform = gen.activity("Inform storehouse and engineering department")
    process_part_list = gen.activity("Process part list")
    check_part = gen.activity("Check required quantity of the part")
    reserve = gen.activity("Reserve part")
    back_order = gen.activity("Back-order part")
    prepare_assembly = gen.activity("Prepare bicycle assembly")
    assemble_bicycle = gen.activity("Assemble bicycle")
    ship_bicycle = gen.activity("Ship bicycle")
    finish_process = gen.activity("Finish process instance")

    part_subprocess = gen.decision_graph(dependencies=[
        (None, check_part),
        (check_part, reserve),
        (check_part, back_order),
        (reserve, None),
        (back_order, None),
    ])

    part_subprocess = gen.self_loop(part_subprocess)
    concurrency = gen.partial_order(dependencies =
        [(part_subprocess,), (prepare_assembly,)]
    )

    final_model = gen.decision_graph(dependencies=[
        (None, create_process),
        (create_process, reject_order),
        (create_process, accept_order),
        (reject_order, finish_process),
        (accept_order, inform),
        (inform, process_part_list),
        (process_part_list, concurrency),
        (concurrency, assemble_bicycle),
        (assemble_bicycle, ship_bicycle),
        (ship_bicycle, finish_process),
        (finish_process, None),
    ])

    return final_model


e6 = (
    "a common error is not to create a partial order for the concurrency between the part handling subprocess and the preparation of the assembly."
)

d7 = (
    "A and B can happen in any order (concurrent). C and D can happen in any order. A precedes both C and D. B "
    "precedes D"
)


def m7():
    gen = ModelGenerator()
    a = gen.activity("A")
    b = gen.activity("B")
    c = gen.activity("C")
    d = gen.activity("D")
    final_model = gen.partial_order(dependencies=[(a, c), (a, d), (b, d)])
    return final_model


e7 = (
    "a common error for this process is to generate a first partial order for modeling the concurrency between"
    " 'A' and 'B', then a second partial order to model the concurrency between 'C' and 'D', then combining these"
    " two partial orders with a large partial that has a sequential dependency from the first order to the second"
    " one. This behavior is not justified and it will imply a wrong dependency ('B' -> 'C'); 'B' and 'C' should"
    " remain independent in the correct partial order."
)

d8 = (
    "A followed by B or C. Then D or G. A can be followed by G. Optionally, after A, we can skip all other activities."
)
def m8():
    gen = ModelGenerator()

    a = gen.activity("A")
    b = gen.activity("B")
    c = gen.activity("C")
    d = gen.activity("D")
    g = gen.activity("G")
    final_model = gen.decision_graph(dependencies=[(None ,a), (a, b), (a, g), (a, c), (b, d), (b, g), (c, g), (c, d), (d, None), (g, None), (a, None)])
    return final_model

e8 = (
    "A common error for this process is to include useless partial order structures instead of using one decision graph to model the whole behavior."
)

d9 = (
    "The process starts with checking part stock availability.",
    "After that, we either cancel the order because we don't have the required parts to produce it,"
    "or we continue with the production. When we cancel the order, we notify the customer via e-mail."
    "If we can produce the machines, we check the production schedule and "
    "we schedule the production of each machine. In the end, we produce the machines." \
    "As soon as the machines are produced, we ship the machines. In the end, we notify the customer via e-mail or via the system."
)


def m9():
    gen = ModelGenerator()

    check_part = gen.activity("Check production schedule")
    schedule_part = gen.activity("Schedule production")
    prod_part = gen.activity("Produce machines")
    ship_part = gen.activity("Ship machines")
    production_block = gen.partial_order(dependencies=[(check_part, schedule_part), (schedule_part, prod_part), (prod_part, ship_part)])

    check_stock = gen.activity("Check part stock availability")
    cancel = gen.activity("Cancel order")
    notify_email = gen.activity("Notify via email")
    notify_system = gen.activity("Notify via system")

    final_model = gen.decision_graph(
        dependencies = [
            (None, check_stock),
            (check_stock, cancel),
            (check_stock, production_block),
            (cancel, notify_email),
            (production_block, notify_email),
            (production_block, notify_system),
            (notify_email, None),
            (notify_system, None),
        ]
    )

    return final_model

e9 = (
    "A common mistake here is to model the decision graph as partial orders of exclusive choices."
    "The sub-model containing the decision graph, i.e., the activities for production, cancelling the order, and the notifications"
    "Is a decision graph, as only one of these paths can be executed in the end: either we start with the production, and then choose between one of the two notificaiton methods, or we cancel the order and notify the customer via e-mail."
    "If we model the decision graph as a partial order of exclusive choices, we lose precision, i.e., the model will allow for more than the described behaviour."
)


# d7 = "An employee purchases a product or service he requires. For instance , a sales person on a trip rents a car. " \
#      "The employee submits an expense report with a list of items , along with the receipts for each item. A " \
#      "supervisor reviews the expense report and approves or rejects the report. Since the company has expense rules , " \
#      "there are circumstances where the supervisor can accept or reject the report upon first inspection. These rules " \
#      "could be automated , to reduce the workload on the supervisor. If the supervisor rejects the report , " \
#      "the employee , who submitted it , is given a chance to edit it , for example to correct errors or better " \
#      "describe an expense. If the supervisor approves the report , it goes to the treasurer. The treasurer checks " \
#      "that all the receipts have been submitted and match the items on the list. If all is in order , the treasurer " \
#      "accepts the expenses for processing ( including , e.g., payment or refund , and accounting ). If receipts are " \
#      "missing or do not match the report , he sends it back to the employee. If a report returns to the employee for " \
#      "corrections , it must again go to a supervisor , even if the supervisor previously approved the report. If the " \
#      "treasurer accepts the expenses for processing , the report moves to an automatic activity that links to a " \
#      "payment system. The process waits for the payment confirmation. After the payment is confirmed , the process " \
#      "ends . "
#
#
# def m7():
#     # Base activities
#     purchase = 'Employee purchases product or service'
#     submit_expense = 'Submit expense report with receipts'
#     review_expense_initial = gen.xor('Initially approve report', 'Initially reject report')
#     edit_report = 'Edit expense report'
#     review_expense_after_edit = gen.xor('Approve report after edit', 'Reject report after edit')
#     treasurer_review = gen.xor('Treasurer accepts expenses', 'Treasurer sends back for corrections')
#     automatic_payment = 'Automatic activity for payment system'
#     wait_payment_confirmation = 'Wait for payment confirmation'
#     end_process = 'End process'
#
#     # Subprocess for editing and re-review after rejection at the initial review
#     edit_and_initial_review = gen.partial_order(list_children=[edit_report, review_expense_initial],
#                                     list_order_dependencies=[(edit_report, review_expense_initial)])
#
#     # Subprocess for editing and re-review after the treasurer sends it back for corrections
#     edit_and_treasurer_review = gen.partial_order(list_children=[edit_report, review_expense_after_edit],
#                                       list_order_dependencies=[(edit_report, review_expense_after_edit)])
#
#     # Combining treasurer review decision with possible loop back for corrections
#     treasurer_decision = DoRedoLoop('Treasurer accepts expenses', edit_and_treasurer_review)
#
#     # Main process flow
#     main_process_flow = gen.partial_order(
#         list_children=[submit_expense, review_expense_initial, treasurer_decision, automatic_payment,
#                        wait_payment_confirmation, end_process],
#         list_order_dependencies=[(submit_expense, review_expense_initial),
#                                  (review_expense_initial, treasurer_decision),
#                                  (treasurer_decision, automatic_payment),
#                                  (automatic_payment, wait_payment_confirmation),
#                                  (wait_payment_confirmation, end_process)])
#
#     # Final model starts with the purchase and follows the main process flow
#     final_model = gen.partial_order(list_children=[purchase, main_process_flow],
#                         list_order_dependencies=[(purchase, main_process_flow)])
#
#     return final_model


SHOTS = [
    (d1, m1, e1),
    (d1_2, m1_2, e1_2),
    (d2, m2, e2),
    (d3, m3, e3),
    (d4, m4, e4),
    (d5, m5, e5),
    (d6, m6, e6),
    (d7, m7, e7),
    (d8, m8, e8),
    (d9, m9, e9)
]

if __name__ == "__main__":
    from pm4py import view_petri_net
    from powl import convert_to_petri_net, view
    model = m9().simplify()
    view(model)
    pn, im, fm = convert_to_petri_net(model)
    view_petri_net(pn, im, fm, format="SVG")
