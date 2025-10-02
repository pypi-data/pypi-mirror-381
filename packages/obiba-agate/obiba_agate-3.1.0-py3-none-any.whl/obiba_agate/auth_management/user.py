"""
Python commands for adding or deleting a User
"""

import json
import obiba_agate.core as core


def user_add_arguments(parser):
    """
    Add agate user management arguments
    """

    parser.add_argument('--name', help='The User Name (required), it must be unique', required=True)
    parser.add_argument('--email', help='The Email (required), it must be unique', required=True)
    parser.add_argument('--upassword', help='The user Password (required if realm is "agate-user-realm")', required=False)
    parser.add_argument('--first-name', help='The user First Name', required=False)
    parser.add_argument('--last-name', help='The user Last Name', required=False)
    parser.add_argument('--realm', help='Realm in which the user will authenticate (default is: "agate-user-realm")',
                        required=False, default='agate-user-realm')
    parser.add_argument('--applications', help='Applications in which the user can sign in, e.g. "opal mica"',
                        required=False, nargs='*')
    parser.add_argument('--groups',
                        help='Members of a group get access to the applications associated to this group, e.g. \
                        "mica-administrator mica-reviewer mica-editor mica-data-access-officer mica-user \
                        opal-administrator"',
                        required=False, nargs='*')
    parser.add_argument('--role', help='A simple user can only access to its own account (default is: "agate-user")',
                        required=False, default='agate-user')
    parser.add_argument('--status', help='Only active users can sign in (default is "ACTIVE")', required=False,
                        default='ACTIVE')


def do_add_command(args):
    """
    Execute add user management command
    """

    request = core.AgateClient.build(core.AgateClient.LoginInfo.parse(args)).new_request()
    request.fail_on_error()

    if args.verbose:
        request.verbose()

    user = {'name': args.name, 'email': args.email, 'role': args.role, 'status': args.status,
            'realm': args.realm}
    if args.first_name:
        user['firstName'] = args.first_name
    if args.last_name:
        user['lastName'] = args.last_name
    if args.applications:
        user['applications'] = args.applications
    if args.groups:
        user['groups'] = args.groups

    if not args.upassword and args.realm == 'agate-user-realm':
        raise Exception("User password is required for Agate's realm.")

    data = {'user': user}
    if args.realm == 'agate-user-realm':
        data = {'password': args.upassword, 'user': user}

    request.post().content_type_json().resource(core.UriBuilder(['users']).build()).content(json.dumps(data))

    response = request.send()
    print(response.content)


def user_delete_arguments(parser):
    """
    Add agate user management arguments
    """

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--name', help='User name')
    group.add_argument('--email', help='User email')


def do_delete_command(args):
    """
    Execute delete user management command
    """

    request = core.AgateClient.build(core.AgateClient.LoginInfo.parse(args)).new_request()
    request.fail_on_error()

    request.get().resource(
        core.UriBuilder(['users', 'find']).query('q', args.name if args.name else args.email).build())

    user_response = request.send()

    new_request = core.AgateClient.build(core.AgateClient.LoginInfo.parse(args)).new_request()
    new_request.fail_on_error()

    new_request.delete().resource(core.UriBuilder(['user', json.loads(user_response.content)['id']]).build())
    response = new_request.send()

    print(response.content)
