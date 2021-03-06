import json
from tutelary.engine import PermissionTree, PolicyBody, Action, Object
from .datadir import datadir  # noqa


def test_permission_set_creation(datadir):  # noqa
    pol = PolicyBody(json=datadir.join('test-policy-1.json').read())
    pset = PermissionTree()
    pset.add(policy=pol)
    assert pset.allow(Action('parcel.view'),
                      Object('Cadasta/Batangas/parcel/123'))
    assert not pset.allow(Action('parcel.edit'),
                          Object('Cadasta/Batangas/parcel/123'))


def test_permission_set_policies_1(datadir):  # noqa
    v = {'organisation': 'Cadasta', 'project': 'Test'}
    pnames = ['default-policy.json', 'org-policy.json', 'project-policy.json']

    sapols = map(lambda f: PolicyBody(json=datadir.join(f).read(),
                                      variables=v),
                 pnames + ['sys-admin-policy.json'])
    sapset = PermissionTree(policies=sapols)

    parcel_view = Action('parcel.view')
    parcel_edit = Action('parcel.edit')
    party_create = Action('party.create')
    admin_assign = Action('admin.assign-role')
    admin_invite = Action('admin.invite')
    statistics = Action('statistics')
    parties = Object('Cadasta/Test/party')
    parcel123 = Object('Cadasta/Test/parcel/123')
    org = Object('org/Cadasta')
    useriross = Object('user/iross')

    assert sapset.allow(parcel_view, parcel123)
    assert sapset.allow(parcel_edit, parcel123)
    assert sapset.allow(party_create, parties)
    assert sapset.allow(admin_assign, useriross)
    assert sapset.allow(admin_invite, useriross)
    assert sapset.allow(admin_invite, org)
    assert sapset.allow(statistics)


def test_permission_set_policies_2(datadir):  # noqa
    v = {'organisation': 'Cadasta', 'project': 'Test'}
    pnames = ['default-policy.json', 'org-policy.json', 'project-policy.json']

    oapols = map(lambda f: PolicyBody(json=datadir.join(f).read(),
                                      variables=v),
                 pnames + ['org-admin-policy.json'])
    oapset = PermissionTree(policies=oapols)

    parcel_view = Action('parcel.view')
    parcel_edit = Action('parcel.edit')
    party_create = Action('party.create')
    admin_assign = Action('admin.assign-role')
    admin_invite = Action('admin.invite')
    statistics = Action('statistics')
    parties = Object('Cadasta/Test/party')
    parcel123 = Object('Cadasta/Test/parcel/123')
    org = Object('org/Cadasta')
    useriross = Object('user/iross')

    assert oapset.allow(parcel_view, parcel123)
    assert oapset.allow(parcel_edit, parcel123)
    assert oapset.allow(party_create, parties)
    assert not oapset.allow(admin_assign, useriross)
    assert oapset.allow(admin_invite, useriross)
    assert oapset.allow(admin_invite, org)
    assert not oapset.allow(statistics)


def test_permission_set_policies_3(datadir):  # noqa
    v = {'organisation': 'Cadasta', 'project': 'Test'}
    pnames = ['default-policy.json', 'org-policy.json', 'project-policy.json']

    dcpols = map(lambda f: PolicyBody(json=datadir.join(f).read(),
                                      variables=v),
                 pnames + ['data-collector-policy.json'])
    dcpset = PermissionTree(policies=dcpols)

    parcel_view = Action('parcel.view')
    parcel_edit = Action('parcel.edit')
    party_create = Action('party.create')
    admin_assign = Action('admin.assign-role')
    admin_invite = Action('admin.invite')
    statistics = Action('statistics')
    parties = Object('Cadasta/Test/party')
    parcel123 = Object('Cadasta/Test/parcel/123')
    org = Object('org/Cadasta')
    useriross = Object('user/iross')

    assert dcpset.allow(parcel_view, parcel123)
    assert dcpset.allow(parcel_edit, parcel123)
    assert not dcpset.allow(party_create, parties)
    assert not dcpset.allow(admin_assign, useriross)
    assert not dcpset.allow(admin_invite, useriross)
    assert not dcpset.allow(admin_invite, org)
    assert dcpset.allow(statistics)


def test_permission_set_policies_4():
    clause = {
        "clause": [
            {
                "effect": "allow",
                "object": ["organization/*"],
                "action": ["organization.*"]
            },
            {
                "effect": "allow",
                "object": ["project/*/*"],
                "action": ["project.*.*"]
            }
        ]
    }
    pol = PolicyBody(json=json.dumps(clause))
    pset = PermissionTree(policies=[pol])

    user_list = Action('project.users.list')
    proj = Object('project/Cadasta/TestProj')
    assert pset.allow(user_list, proj)
