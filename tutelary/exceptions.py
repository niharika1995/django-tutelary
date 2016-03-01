class TutelaryException(Exception):
    pass


class EffectException(TutelaryException):
    """Exception raised when an effect type other that ``allow`` or
    ``deny`` is encountered in a JSON policy body.

    """
    def __init__(self, effect):
        super(EffectException, self).__init__(
            "illegal permission effect: '" + effect + "'"
        )


class PatternOverlapException(TutelaryException):
    """Exception raised when overlapping action or object patterns are
    used in a single policy clause.

    """
    def __init__(self, exc_type):
        super(PatternOverlapException, self).__init__(
            "overlapping " + exc_type + " patterns in policy clause"
        )


class PolicyBodyException(TutelaryException):
    """Exception raised for miscellaneous errors in JSON policy bodies."""
    def __init__(self, msg=None, lineno=None, colno=None):
        if msg is not None:
            super(PolicyBodyException, self).__init__(
                "illegal policy body: " + msg
            )
        else:
            super(PolicyBodyException, self).__init__(
                "illegal policy body: " +
                "line " + str(lineno) + ", column " + str(colno)
            )


class VariableSubstitutionException(TutelaryException):
    """Exception raised for illegal variable substitutions when using JSON
    policy bodies.

    """
    def __init__(self):
        super(VariableSubstitutionException, self).__init__(
            "illegal variable substitution in policy body"
        )


class DecoratorException(TutelaryException):
    """Exception raised if the ``permissioned_model`` decorator is used
    without the required ``TutelaryMeta`` class member being included
    in the model.

    """
    def __init__(self, decorator, msg):
        super(DecoratorException, self).__init__(
            "error expanding decorator '" + decorator + "': " + msg
        )


class PermissionObjectException(TutelaryException):
    """Exception raised by the ``permissioned_model`` decorator if a
    ``permissions_object`` property in the ``actions`` list refers to
    a non-existent model field, or to a field that is not a foreign
    key or one-to-one relation field.

    """
    def __init__(self, prop):
        super(PermissionObjectException, self).__init__(
            "invalid permissions_object property '" + prop +
            "' in permissioned_model"
        )
