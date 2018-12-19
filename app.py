from bottle import route, run, request, abort, static_file

from fsm import TocMachine



VERIFY_TOKEN = "HELLO"
machine = TocMachine(
    states=[
        'user',
        'instruction',
        'stateNS',
        'stateNSbuy',
        'stateNSbuyname',
        'stateNSsell',
        'stateNSsellname',
        'statePS',
        'statePSbuy',
        'statePSbuyname',
        'statePSsell',
        'statePSsellname',
        'stateXB',
        'stateXBbuy',
        'stateXBbuyname',
        'stateXBsell',
        'stateXBsellname'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'instruction',
            'conditions': 'is_going_to_instruction'
        },
        {
            'trigger': 'advance',
            'source': 'instruction',
            'dest': 'stateNS',
            'conditions': 'is_going_to_stateNS'
        },
        {
            'trigger': 'advance',
            'source': 'stateNS',
            'dest': 'stateNSbuy',
            'conditions': 'is_going_to_stateNSbuy'
        },
        {
            'trigger': 'advance',
            'source': 'stateNS',
            'dest': 'stateNSsell',
            'conditions': 'is_going_to_stateNSsell'
        },
        {
            'trigger': 'advance',
            'source': 'stateNSbuy',
            'dest': 'stateNSbuyname',
            'conditions': 'is_going_to_stateNSbuyname'
        },
        {
            'trigger': 'advance',
            'source': 'stateNSsell',
            'dest': 'stateNSsellname',
            'conditions': 'is_going_to_stateNSsellname'
        },
        {
            'trigger': 'advance',
            'source': 'instruction',
            'dest': 'statePS',
            'conditions': 'is_going_to_statePS'
        },
        {
            'trigger': 'advance',
            'source': 'statePS',
            'dest': 'statePSbuy',
            'conditions': 'is_going_to_statePSbuy'
        },
        {
            'trigger': 'advance',
            'source': 'statePS',
            'dest': 'statePSsell',
            'conditions': 'is_going_to_statePSsell'
        },
        {
            'trigger': 'advance',
            'source': 'statePSbuy',
            'dest': 'statePSbuyname',
            'conditions': 'is_going_to_statePSbuyname'
        },
        {
            'trigger': 'advance',
            'source': 'statePSsell',
            'dest': 'statePSsellname',
            'conditions': 'is_going_to_statePSsellname'
        },
        {
            'trigger': 'advance',
            'source': 'instruction',
            'dest': 'stateXB',
            'conditions': 'is_going_to_stateXB'
        },
        {
            'trigger': 'advance',
            'source': 'stateXB',
            'dest': 'stateXBbuy',
            'conditions': 'is_going_to_stateXBbuy'
        },
        {
            'trigger': 'advance',
            'source': 'stateXB',
            'dest': 'stateXBsell',
            'conditions': 'is_going_to_stateXBsell'
        },
        {
            'trigger': 'advance',
            'source': 'stateXBbuy',
            'dest': 'stateXBbuyname',
            'conditions': 'is_going_to_stateXBbuyname'
        },
        {
            'trigger': 'advance',
            'source': 'stateXBsell',
            'dest': 'stateXBsellname',
            'conditions': 'is_going_to_stateXBsellname'
        },
        {
            'trigger': 'go_back',
            'source': [
                'stateNSbuyname',
                'stateNSsellname',
                'statePSbuyname',
                'statePSsellname',
                'stateXBbuyname',
                'stateXBsellname'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    run(host="localhost", port=5000, debug=True, reloader=True)
