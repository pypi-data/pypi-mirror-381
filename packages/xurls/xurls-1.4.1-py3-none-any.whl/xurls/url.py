"""
Helper classes to work with Url's.

Allows you to easily create, work with and append Urls together.

Main classes:
- `Url`

## Path Formatting Placeholders:
[path-formatting-placeholders]: #path-formatting-placeholders

The `path` can contain template formatting placeholders, just like you would do in a
normal python string. These ones MUST be named, however, and not positional formatting
placeholders.

At some point in the future, I will probably support formatting placeholders for
a query value. For now, it's only for the path.

Here is an example:
`"http://api.com/v1/accounts/{id}"`

If later on, we add a query like this to the Url:
`Url.query_add`('id', 1)

And then call `url.url()`, we will get back this:
`"http://api.com/v1/accounts/1"`

You can also pass in a secondary/backup list of key/values into the .url(...) method,
like so:

>>> url = Url("https://api.com/some/endpoint/{id}")
>>> url.url(secondary_values={'id': 9})
"https://api.com/some/endpoint/9"

It can also be an object, which in this case it will look for an attribute of `id`.

`Url.url` will return `None` if it can't construct the Url due to an absent format
value that it can't find. In this way, you could have a list of Url's and the first
one that can be formatted is the one you use.

You can also use `Url.is_valid` to see if the url is valid in a more efficent way,
as it won't need to format the full url to determine this.

Value for formatting placeholders come from these sources:

1. First look in Url's query values (`Url.query`), looking for a value with same key-name.
3. We next look in any secondary_values passed into the `Url.url` method for the value
    we need if not found in query-value.
2. Finally, we will fallback attached values, you can attach values to a mutable url
    via `Url.is_valid`; see doc-comment in that method for more details.

.. todo:: At some point in the future I'll probably support place-holders for
    query-key/values.  The `format_placeholders` argument would also control
    this too once we get around to supporting that.

"""
from __future__ import annotations
from typing import (
    Type,
    Optional,
    Union,
    TypeVar,
    Dict,
    Iterable,
    get_type_hints,
    List,
    Set,
    Sequence,
    Any,
    Iterator,
)
import datetime as dt
from copy import copy
from urllib import parse as urlparser
from types import MappingProxyType
from dataclasses import dataclass
import string
from uuid import UUID
from warnings import warn

from xloop import xloop

# I'm not going to worry about url 'parameters' for now,
# Url parameter example:  "http://www.google.com/some_path;paramA=value1;paramB=value2"
from xsentinels import Default

T = TypeVar("T")

SecondaryValues = Union[object, dict, Sequence[object]]


class _FormattedQueryValue:
    """
    Formats query values into the final formatted string.

    `_FormattedQueryValue.url_query` is what `Url` calls when it needs to format it's self
    into a string via `Url.url`. It will be called on the first item (or only item) if it's
    a _FormattedQueryValue type value.  If it's not, it will use a plain/default instance of
    `_FormattedQueryValue`.

    By default `_FormattedQueryValue.url_query` will call `_FormattedQueryValue.url_query_value`
    for each value encountered (and if the original value was a list, for each item in the list).

    It then combines these together into a single string by a the
    `UrlFormattingOptions.list_value_delimiter` and if there is more than one value
    adds a `UrlFormattingOptions.list_key_suffix` to the end of key if the key does not
    already have that suffix.

    .. note:: Thinking about putting in an ability to change the default formatter via a
        `xinject.context.Resource`. That way it could easily be overridden via a
        `xinject.context.Context`.  I'll do that if/when we need it.
        For now the default _FormattedQueryValue is just a plain instance that is shared
        via a private module attribute.
    """

    def url_query(
        self, *, key: str, url: Url, url_options: UrlFormattingOptions, values: List[Any]
    ) -> Query:
        """
        If `_FormattedQueryValue` encountered as a query value as the first or only value while
        trying to convert a Url to a string we will call `url_query` on that value.

        If the first item is not a `_FormattedQueryValue` (such as a plain `str`) then and instance
        of this class (not a sub-class) will be directly used for format the query value into
        what is needed in final formatted Url by returning a dict of the needed key/str-values
        to append to final formatted Url.

        It's expected this will return a dict with whatever key/values are needed to
        represent the value in a url query.

        By default (unless method overriden via a sub-class) this method will go though each
        value passed in under `values` paramter and call `_FormattedQueryValue.url_query_value`
        on each one. If there is only one value, this still still happen but just for that single
        value. Method `_FormattedQueryValue.url_query_value` is expected to convert this value
        into a string. It's possible to have a subclass in simple cases to only just override
        `_FormattedQueryValue.url_query_value` and let us call that for each value. We would
        then combine the strings produced into a single string (like you would expect).

        Args:
            key (str): Key that is currently being used for the query name for our value (self).
            url (Url): Url that is being formatted, so you can examine it if needed
            url_options (UrlFormattingOptions): Options that are being used to format the url.
            values (List[Any]): A list of the query values as orginally set into the Url;
                this means the values can be anything.
        Returns:
            A dictionary with whatever key/values you need.  Keep in mind that if the key
            name(s) returned conflict with other keys, only one will be selected and the others
            ignored, depending on the order the original options were defined in. Values with
            new keys added to the original Url's query later will take priority over earlier ones.

            Example:

            >>> class MyValueType(_FormattedQueryValue):
            ...     def url_query(self, *args, **kwargs):
            ...         return {'key-1': 'hello!'}
            >>>
            >>> my_url = Url()
            >>> my_url.query_add('key-1', "my-value")
            >>> my_url.query_add('key-2', MyValueType())

            In this example, type `MyValueType` implements _FormattedQueryValue and returns

            >>> {'key-1': 'hello!'}

            Since it's defined after adding `my-value` it will overwrite it with
            `hello!`

            >>> my_url.url()
            "?key-1=hello"
        """
        delimiter = url_options.list_value_delimiter
        suffix = url_options.list_key_suffix
        keep_suffixes = url_options.list_key_suffixes_to_keep
        final_items = []

        for item in values:
            call_on = self
            if isinstance(item, _FormattedQueryValue):
                call_on = item
            str_val = call_on.url_query_value(url=url, url_options=url_options, value=item)

            if not str_val:
                continue
            final_items.append(str_val)

        if len(final_items) == 1:
            new_val = final_items[0]
        else:
            # If we already end with suffix, don't add it.
            if not key.endswith(suffix):
                add_suffix = True
                for s in keep_suffixes:
                    if key.endswith(s):
                        add_suffix = False
                        break

                if add_suffix:
                    key = key + suffix

            # todo: consider raising an exception if we have blank/no delimiter.
            if delimiter:
                new_val = delimiter.join(final_items)
            else:
                # We send back a list if there is no delimiter, it will format url like this
                # with duplicate keys in the string:
                #   '?key:final_items-1&key:final_items-2&....'
                new_val = final_items

        return {key: new_val}

    def url_query_value(self, *, url: Url, url_options: UrlFormattingOptions, value: Any) -> str:
        """
        `_FormattedQueryValue.url_query` calls this method is call for each value in the query.
        If a query item has a list with more than one values this is normally called on each
        value in that list and then combined together via url formatting options.

        Whatever value is returned will be incorporated into the query via the
        UrlFormattingOptions: `list_key_suffix` and `list_value_delimiter` attributes inside
        `_FormattedQueryValue.url_query`.

        Args:
            url: Url that is being formatted, so you can examine it if needed
            url_options: Options that are being used to format the url.
            value: The specific value to format. if this value is a _FormattedQueryValue then
                it's guaranteed that `self` will be the same as the passed in value.
                If some values inside query-value of url are a `_FormattedQueryValue` and
                others are not then it's possible for this method to be called where the
                `value` is that other value and self will be the first _FormattedQueryValue
                in the query list.  If the first value in the query list is something else
                then the default _FormattedQueryValue is used (just a plain instance),
                and that's what `self` will be.
        """
        if isinstance(value, dt.date):
            return value.isoformat()
        elif value or isinstance(value, int):
            return str(value)


_default_query_formatter = _FormattedQueryValue()
""" Class that's used to format query values when the first/only value is a plain str (string). """

QueryValue = Union[
    str,
    int,
    dt.date,
    _FormattedQueryValue,
    None,
    UUID,
    Iterable[str | int | UUID | dt.date | _FormattedQueryValue],
]
""" A query value can be either a str, or a list of str.

    If it is a list of str, then the key will have __in appended and the values will be delimited
    by a comma ',' if Url.use_in_operator_for_query_lists is True, ie: `?someKey__in=A,B`.

    Otherwise they will be duplicated, ie: `?someKey=A&someKey=B`.

    If Url.use_in_operator_for_query_lists is False, we instead duplicate the key
    for each value in the list in final url, ie: (1, 2) turns into: 'a_key=1&a_key=2'.

    use_in_operator_for_query_lists is True by default.
"""

Query = Dict[str, QueryValue]
""" Type that represents the entire query portion of a Url.
"""


@dataclass
class UrlFormattingOptions:
    # TODO: Allow for a configurable formatting callback function/object.

    list_key_suffix: str = '__in'
    """ What to strip/append to query key-name if the value is a list.
        When parsing a Url, if the key name does not end with this, we won't try to split the value
        by the `list_value_delimiter`, the value will be left unchanged.

        When parsing a Url, the list_key_suffix will be striped from the key-name. When
        constructing the Url into a string, list_key_suffix will be added to a key-name if the
        value is a list.

        Default is '__in', which is the standard way Django Rest Framework's filters work.
    """

    list_key_suffixes_to_keep = [
        '__fields__include',
        '__fields__only',
        '__fields__exclude',
        '__in!'
    ]
    """ Suffixes listed here can implicitly take a delimited list of values
        without using the generalized `UrlFormattingOptions.list_key_suffix` (see above).

        The `UrlFormattingOptions.list_key_suffix` won't be used if a key ends with one of
        these keys, but instead the list will be directly formatted/parsed directly out of
        the value without modifying the key.
    """

    list_value_delimiter: str = ','
    """ This tells the Url the character to split query value by.

        If there is no delimiter in value, then a list with a single value is the result.
        Keep in mind that list won't be parsed from a queries value if the queries key-name
        does not end with `list_key_suffix`.  The `list_key_suffix` is what controls if the
        query value is a list or not.

        Default is a comma `,`.
    """


DefaultQueryValueListFormat = UrlFormattingOptions()
""" The default if `formatting_options` is None.

    Produces a format that does this when you have a query-key with multiple values:
        "http://host/path?key-name__in=value1,value2"

    When you do this:
        `query_add('key-name', ['value1', 'value2'])`
"""

DuplicateKeyNamesQueryValueListFormat = UrlFormattingOptions(
    list_key_suffix='', list_value_delimiter=''
)
""" Produces a format that does this when you have a query-key with multiple values:
        "http://host/path?key-name=value1&key-name=value2"

    When you do this:
        `query_add('key-name', ['value1', 'value2']`
"""

HTTPMethodType = str

# Standard Methods
HTTPGet = 'GET'
HTTPPatch = 'PATCH'
""" Represents http PATCH method. """
HTTPDelete = 'DELETE'
HTTPPost = 'POST'
HTTPPut = 'PUT'


class Url:
    """
    Allows you to easily create, work with and append Urls together.

    You can pass a normal Url or string into the first argument of `Url.__init__`, and if you do
    it as a string it will be parsed as a Url and it's components will be set into the
    returned as a Url with it's various components parsed into Url's various attributes.

    There is also a parameter for each Url component attribute in the `Url.__init__` method.

    If no value is provided for a particular url component, it will be assigned a `None` value.

    Use `Url.url()` method to get a url `str` back from components.

    For more details on path features,
    see [Path Formatting Placeholders](#path-formatting-placeholders)

    ## Mutating Methods

    A big way to use Url is to `Url.append_url` `Url`'s together.  You can then take
    different `Url`'s that have different components and construct a final `Url` to use.

    When appending a Url to another [via `Url.append_url`], if any particular component
    has a None value, it will not change the Url it's being appended to for that particular
    component. This allows you to append Urls together and only relevant/set-values will
    be what's appended. This allows you to construct Urls based on pieces of Urls to construct
    the final Url.

    When you append a Url, the path and query and methods are treated in a special way:

    - `Url.path`: it will be appended to the destination Url via
        `Url.append_path`, and therefore, the path will be appended onto the existing
        path (with a `/` if needed to separate them).

    - `Url.query`: Keys will be added via `Url.query_add`, and therefore the only
        keys that will be replaced are ones where the same key-name exists in both Urls.
        Otherwise, the keys are 'added' together.

    - `Url.methods`: This will get union'd with the existing `methods` in the destination
        url.

    The methods that mutate self [such as 'append_path', etc] return self, so you can chain
    them together with other mutating methods.

    Example Usages:
    >>> urlc = Url()
    >>> urlc.scheme = 'http'
    >>> urlc.host = 'www.google.com'
    >>> urlc.format()
    "http://www.google.com"
    >>> urlc = Url("http://www.google.com").append_url("/hello")
    >>> urlc.format()
    "http://www.google.com/hello"

    """

    @classmethod
    def ensure_url(
        cls: Type[T],
        value: Optional[UrlStr],
        *,
        default_formatting_options: UrlFormattingOptions = Default,
    ) -> T:
        """Will check to see if the passed in value is a `Url` (depending on the
            class you call `Url.ensure_url` on). If so, will return value unchanged.
            This is an optimization and the reason to use this method over just constructing
            a new `Url` and passing the value into that. If the value is already a Url,
            and it's formatting_options don't need to be set to `default_formatting_options`
            it will just return it without any extra work.

            If not then will create a new instance of cls and pass value to `__init__`
            and return result.

            ### If you provide `default_formatting_options`:

            If you pass in a `str` to this method, then any `formatting_options` you passed in
            will be checked and used if provided.

            If you pass in a Url, and it has not explicitly set formatting_options, we
            will make a copy of passed in Url and set `default_formatting_options` on it
            and return copy.

            Otherwise, Url will use the usual `DefaultQueryValueListFormat` for the default format.

        Args:
            value: You can pass in a UrlStr (which is either a `str` or `Url`), and you will get
                back a `Url` object from it. If the value is exactly the same as the class you call
                this class method on, you will get it back unchanged. If not then we create a new
                object of type `cls` and give value to it as a init parameter.

                If `value` is not a `Url` or `str`, we will try and convert it to a `str` for
                you in an attempt to extract a url string from the passed in object.

            default_formatting_options (UrlFormattingOptions): Formatting options to use IF
                passed in value is a string.  If the passed in value is a Url object, we use
                whatever it has set on it. If no formatting options are set on the `Url` object
                that is passed in, and you pass in a default_formatting_options, we will copy
                passed in Url and set that formatting option on it, and return copy.

        Returns:
             Url: Object of same type as `cls`, which is the class you called `Url.ensure_url` on.
        """
        if type(value) is cls and (not default_formatting_options or value.formatting_options):
            return value

        if isinstance(value, Url) and value.formatting_options:
            # Url already has explicitly set formatting-options, keep whatever it has.
            return cls(value)

        # Otherwise, we are some other non-Url value (ie: a `str` probably),
        # try tp convert value to string and any default_formatting_options the user provided.
        return cls(value, formatting_options=default_formatting_options)

    def __init__(
        self,
        url: Union[str, Url] = None,
        *,
        scheme: str = Default,
        username: str = Default,
        password: str = Default,
        host: str = Default,
        port: int = Default,
        path: str = Default,
        query: Query = Default,
        fragment: str = Default,

        metadata: dict = Default,
        formatting_options: UrlFormattingOptions = Default,

        # Params below are extra metadata about Url that is useful to communicate about:
        # TODO: Find a more generalized way to include 'mergeable'/'appendable' metadata
        #   in the Url object; For now keeping them, but need to remove in the
        #   next major release.
        singular: bool = None,
        methods: Union[str, Iterable[str]] = None,
    ):
        """
        # `__init__` Specifics

        Pass in a single 'url' or pass in the individual components.

        If you pass in both, the individual components [kw-args] will take precedence.
        If you pass in a query parameter arg, it will completely replace entire query from
        any that were provided in `url` string. Same goes with the 'path'.
        Use 'append_url(...)' to easily merge/append query/paths together.

        If `xsentinels.Default` is left in place, then that value will be ignored and not replace
        anything that was parsed for that component from `url` string. Unless the 'url'
        pass in defined that particular component it will be set to None. When you append
        a Url on another with values set to None, it will not 'append' them into the Url.

        If you pass in a None, we will replace that particular value with a None inside the
        Url.

        All parameters are optional. Providing no parameters at all creates a completely
        blank Url. If you ask for the .url() of a blank Url, an empty string is returned.

        Here is an example of all of these basic Url components in their proper place:
        `scheme://username:password@host:port/path?query#fragment`


        Args:
            url (str, Url): A normal Url formatted string or Url object;
                ie: "www.google.com/hello".

                If provided, forms the basis of the Url.
                All other parameters will over-write that particular
                component of the url provided here
                [ie: the other parameters take priority].

            scheme: Replaces/Sets scheme on new Url object.
            password: Replaces/Sets password on new Url object.
            host: Replaces/Sets host on new Url object.
            port: Replaces/Sets port on new Url object.
            path: Replaces/Sets path on new Url object.
                Path's can have variable placeholders in them, see
                [Path Formatting Placeholders](#path-formatting-placeholders).

            fragment: Replaces/Sets fragment on new Url object.
            query:  Replaces/Sets query on new Url object.

            formatting_options:
                Way to configure how a query value can be split up into a
                list when parsing a url, and back again when reconstructing the url into a string.
                For details, see the `UrlFormattingOptions` class.

                If set with None, `Url` class uses `DefaultQueryValueListFormat` by default
                for it's formatting options.

            singular: (deprecated: need more generalized way to include metadata)
                Provides a hint to indicate if the body of the request/response should be a
                list or a single object. If 'None' [default], then the underlying system will do
                it's best to guess based on other factors.

            methods: (deprecated: need more generalized way to include metadata)
                If useful, you can provide a hint of which HTTP methods this Url is
                valid for. Defaults to an empty set. When you append methods to another Url,
                the result is a union of both sets of methods from the two Url's.
        """

        if formatting_options is not Default:
            self._formatting_options = formatting_options

        if methods is not None:
            warn(
                "Url.methods deprecated pending a more generalized way to include metadata.",
                DeprecationWarning, 2
            )
            self._set_methods(methods)
        else:
            self._methods = set()

        if singular not in (None, Default):
            warn(
                "Url.singular deprecated pending a more generalized way to include metadata.",
                DeprecationWarning, 2
            )
            self._singular = singular

        if isinstance(url, str):
            result: urlparser.ParseResult = urlparser.urlparse(url)

            self._scheme = result.scheme or None

            value = result.username
            self._username = urlparser.unquote(value) if value else value

            value = result.password
            self._password = urlparser.unquote(value) if value else value

            self._host = result.hostname
            self._port = result.port
            self._path = result.path or None
            self._fragment = result.fragment or None
            self._query = self._parse_string_into_query(result.query)
            self._metadata = {}
        elif isinstance(url, Url):
            self._copy_from_url(url)
        elif url in (None, Default):
            self._query = {}
            self._metadata = {}
        else:
            raise TypeError(f"Type passed into Url(...) is not a str/Url/None, but ({type(url)}).")

        if scheme is not Default:
            self._scheme = scheme

        if username is not Default:
            self._username = username

        if password is not Default:
            self._password = password

        if host is not Default:
            self._host = host

        if port is not Default:
            self._port = port

        if path is not Default:
            self._path = path

        if fragment is not Default:
            self._fragment = fragment

        if query is not Default:
            self._set_query(query)

        if metadata is not Default:
            self._metadata = metadata
    # ----------------------------------------
    # --------- Basic Url attributes ---------

    @property
    def scheme(self) -> Optional[str]:
        return self._scheme

    @property
    def username(self) -> Optional[str]:
        return self._username

    @property
    def password(self) -> Optional[str]:
        return self._password

    @property
    def host(self) -> Optional[str]:
        return self._host

    @property
    def port(self) -> Optional[int]:
        return self._port

    @property
    def path(self) -> Optional[str]:
        """Path's can have variable placeholders in them, for more details see
        [Path Formatting Placeholders](#path-formatting-placeholders).
        """
        return self._path

    @property
    def fragment(self) -> Optional[str]:
        return self._fragment

    @property
    def query(self) -> MappingProxyType:
        """Returns a live-updating mapping of the url query values as a read-only proxy map."""
        # Mapping proxy is a read-only view of the passed in dict.
        # This will LIVE update the mapping if _query is directly changed!
        return MappingProxyType(self._query)

    @scheme.setter
    def scheme(self, value: Optional[str]):
        self._scheme = value
        pass

    @username.setter
    def username(self, value: Optional[str]):
        self._username = value
        pass

    @password.setter
    def password(self, value: Optional[str]):
        self._password = value
        pass

    @host.setter
    def host(self, value: Optional[str]):
        self._host = value
        pass

    @port.setter
    def port(self, value: Optional[int]):
        self._port = value
        pass

    @path.setter
    def path(self, value: Optional[str]):
        """Path's can have variable placeholders in them, for more details see
        [Path Formatting Placeholders](#path-formatting-placeholders).
        """
        self._path = value
        self._path_changed()
        pass

    @fragment.setter
    def fragment(self, value: Optional[str]):
        self._fragment = value
        pass

    @query.setter
    def query(self, value: Query):
        """Each value in query dictionary can be either a str/int, or a list of str/int.
        If it is a list, see self.formatting_options for details on what happens.
        """
        # Filter out None values from dictionary.
        self._set_query(value)

    # ---------------------------------
    # --------- Configuration ---------

    @property
    def metadata(self) -> dict:
        return self._metadata

    @metadata.setter
    def metadata(self, value: dict):
        assert isinstance(value, dict)
        # Shallow Copy the dict into self.
        self._metadata = copy(value)

    @property
    def singular(self) -> Optional[bool]:
        """This is a hint to the underlying system that the query will return a singular object
        instead of potentially many.  If this is None, then underlying system may try to
        inspect results to try and determine if it's many or one/singular.

        todo: Implement 'None' value in api.RestClient, right now it treats None as False.
        """
        return self._singular

    @singular.setter
    def singular(self, value: Optional[bool]):
        warn(
            "Url.singular deprecated pending a more generalized way to include metadata.",
            DeprecationWarning, 2
        )
        self._singular = value

    @property
    def formatting_options(self) -> UrlFormattingOptions:
        """
        This tells Url how to encode/decode multiple values [ie: list] for a particular
        query name-key.

        If `formatting_options` is None, then by default `DefaultQueryValueListFormat`
        will be used.

        Just like other Url attributes, if `formatting_options` is None, it will, and you
        append this Url to another Url, `formatting_options` will not change.

        A query value can be either a str/int, or a list of str/int.

        If it is a list of str/int, and if self.formatting_options is True,
        then the key will have a suffix appended [`__in` by default] and the values will
        be delimited by a string [`,` - comma by default].

        If self.formatting_options is None, we instead duplicate the key
        for each value in the list in final url.

        Examples for `key='someKey', value=['A', 'B']`:

        - self.formatting_options is None:
            `?someKey=A&someKey=B`

        - self.formatting_options is QueryValueListFormat('__in', ','):
            `?someKey__in=A,B`.
        """
        return self._formatting_options

    @formatting_options.setter
    def formatting_options(self, value: UrlFormattingOptions):
        self._formatting_options = value

    @property
    def methods(self) -> Optional[tuple]:
        # Return a read-only copy of the methods.
        return tuple(self._methods)

    @methods.setter
    def methods(self, value: Union[Iterable[str], str]):
        warn(
            "Url.methods deprecated pending a more generalized way to include metadata.",
            DeprecationWarning, 2
        )
        self._set_methods(value)

    def methods_contain(self, method: str) -> bool:
        """Returns True if method is one of my methods, or if I have not assigned methods.
        Otherwise, returns False.

        It's faster to use this method then to get all methods and look yourself since I
        use a set internally and can more quickly lookup things in the set.
        """
        if not self._methods:
            return True

        return method in self._methods

    def methods_have_one_in(self, methods: Set[str]) -> bool:
        return not self._methods.isdisjoint(methods or set())

    @property
    def secondary_values(self) -> SecondaryValues:
        """Returns any SecondaryValues that have been attached to Url.
        See `self.is_valid(...)` and/or `self.url(...)` for more details.
        """
        return self._secondary_values

    # ------------------------------
    # --------- Copy/Utils ---------

    def copy(self) -> Url:
        """ We are immutable, so return self without needing to copy. """
        return Url(self)

    def copy_mutable(self) -> Url:
        """ Returns a copy of self as a Url. """
        return Url(self)

    def __copy__(self):
        # Creates a new object of type self, with self as first param.
        # This should make a copy of self.
        return Url(self)

    # ---------------------------------
    # ------------ Methods ------------

    # todo: Not sure if this really should be here or not...
    def query_id_if_singular(self):
        val = self._query.get('id')
        if val is None:
            return None

        if isinstance(val, (str, int)):
            return val

        new_val = list(map(str, val))
        if len(new_val) == 1:
            return new_val[0]

        return None

    def is_valid(
            self, secondary_values: SecondaryValues = Default, attach_values: bool = False
    ) -> bool:
        """
        A more efficient way to determine if we can produce a valid url string.
        The efficiency comes from not needing to actually format and produce the url string.

        Return True if self.url() would return a valid url, else False.

        The Url version of this method allows you to 'attach' the secondary values
        to the url. If so, will use the attached values when calling self.url(...) and passing
        no secondary values into that method.

        Args:
            secondary_values: If query does not have a needed value to satisfy a formatting
                placeholder, we will look at values in here.
                It can be a object, dict or a sequence of objects.
                If the object(s) or dict has the needed value, then we will use that to satisfy
                the url placeholder.

            attach_values: If `True`, will 'attach' the secondary values **IF** url is valid with
                them.
                Attaching means that they are the default secondary values used when generating
                the Url or when calling is_valid(...) in the future.

                If attach_values is a Class/Object, it will directly set this value into the new
                copy.
                We will do a shallow-copy IF the value is a dict/list.

        Returns:
            True: `Url` is valid and you can call `Url.url` without a problem
                (with same secondary_values if you did not attach them).
            False: `Url` is invalid, it needs more formatting params or there is some other issue.
        """

        format_map = self._formatted_map(secondary_values=secondary_values)
        if format_map and attach_values:
            # Do a shallow copy if it's a list/dict, like we document we do.
            # We don't make a copy for anything else (like a normal object).
            if isinstance(secondary_values, (list, dict)):
                secondary_values = copy(secondary_values)
            # Attach these as the default secondary_values when formatting self.url()
            self._secondary_values = secondary_values
        return format_map is not None

    def url(
        self,
        *,
        default_scheme: str = None,
        secondary_values: SecondaryValues = Default,
        allow_invalid_url: bool = False,
    ):
        warn(
            "Url.url is deprecated, instead use `Url.format` "
            "or directly convert url object to a str.",
            DeprecationWarning, 2
        )

        return self.format(
            default_scheme=default_scheme,
            secondary_values=secondary_values,
            allow_invalid_url=allow_invalid_url
        )

    def format(
        self,
        *,
        default_scheme: str = None,
        secondary_values: SecondaryValues = Default,
        allow_invalid_url: bool = False,
    ) -> Optional[str]:
        """
        Returns url as a string, with an optional `default_scheme`.

        You can get the same value (with all args left at their default values)
        by simply converting object to a string:

        ```python
        some_url = Url("https://www.some-url.com/")

        # Ways to convert to string:
        print(some_url.format())
        print(str(some_url))
        print(f'Formatted Url: {some_url}')
        ```

        Output:
        ```
        https://www.some-url.com/
        https://www.some-url.com/
        Formatted Url: https://www.some-url.com/
        ```

        Path's can have variable placeholders in them, for more details see
        [Path Formatting Placeholders](#path-formatting-placeholders)

        If any placeholder can't find it's value, we return `None`.
        If you always need a string, pass False to the `format_placeholders` argument.

        At some point in the future I'll probably support place-holders for
        query-key/values.  The `format_placeholders` argument would also control
        this too once we get around to supporting that.

        Args:
            default_scheme: If self.scheme is None or blank, use this passed in default scheme.

            secondary_values: If path needs formatting and there is no valid query value I can use,
                see if obj has an attribute with a valid value. The attribute name will be same as
                formatting key name.

                If `None`, will check to see if we have any attached self.secondary_values and
                try to use that if it has something when needed.

            allow_invalid_url: If `True`: Always return a `str` with as much as the url formatted
                as possible. We will never return None in this case.

                If `False` (default): Always return a fully formatted url, and if we can't do
                that then return `None` instead.

                .. important:: If you indirectly convert a `Url` object into a string via
                    `f"some url {url_obj}"`, that will pass True to `allow_invalid_url`
                    in order to always produce a non-None string, as Python requires this.
                    This is mostly used when logging url objects.
                    Code that always requires a valid url should use this method to explicitly
                    format the `Url` object into a fully-formatted url string!
        Returns:
            Normal string as a fully constructed url.

            If `None` is returned, the Url could not be formatted (see `Url.is_valid`).
            There is a missing or invalid value for one of the required formatting key-names.

            See Url class doc section
            [Path Formatting Placeholders](#path-formatting-placeholders).
            for more details.
        """

        used_query_keys: List[str] = []

        path = self._formatted_path(
            secondary_values=secondary_values, query_keys_used=used_query_keys
        )
        # If we can't format the path due to finding all placeholders,
        # then we return None to indicate we can't format the url.
        if path is None:
            if not allow_invalid_url:
                return None
            # Use unformatted / raw url path as we can't format it and we have allow_invalid_url.
            path = self.path

        netloc = ''
        if self._host is not None:
            netloc = self._host

        userpass = None
        if self._username is not None:
            userpass = urlparser.quote(self._username)

        if self._password is not None:
            userpass = f"{userpass}:{urlparser.quote(self._password)}"

        if userpass is not None:
            netloc = f"{userpass}@{netloc}"

        if self._port is not None:
            netloc = f"{netloc}:{self._port}"

        scheme = self._scheme or default_scheme or ''

        fragment = self._fragment or ''
        query_dict = self._query

        if used_query_keys:
            # Filter out any keys that we should ignore.
            # Filters dict and makes a copy at the same time, exactly what we need!
            query_dict = {k: query_dict[k] for k in query_dict if k not in used_query_keys}

        query = self._format_query_into_string(query_dict)

        return urlparser.urlunparse((scheme, netloc, path or '', '', query, fragment))

    def __str__(self):
        """
        Will return self.url(), which should return a formatted url string.

        If that returns None, it means we have some part of the Url that can't be formatted,
        so we then return an unformatted/raw version of the Url.

        This means placeholders like `hello/{some_value}/`, if we don't have a value
        for `{some_value}` then we would have to return the Url with the placeholder as-is
        instead of formatting the Url and replacing `{some_value}` with the real value.
        """
        # If we can't generate a valid url, then return the best invalid version we have.
        return self.url(allow_invalid_url=True)

    def __repr__(self):
        return f"{type(self).__name__}('{self}')"

    # ---------------------------------------------
    # --------- Advanced Mutation Methods ---------

    def set_methods(self, methods: Union[Iterable[str], str], *args):
        """Sets methods and returns self, so you can chain it with other mods.
        You can pass in an iterable or a direct string, for any number of arguments.
        We will iterate each argument if it's not a string to combine all of them
        together in one list, which will be set on self.methods.

        `self` is returned, so you can chain this with other method calls.
        """
        self._set_methods(xloop(methods, args))
        return self

    def set_singular(self, value: Optional[bool]) -> Url:
        """Sets singular to value.
        `self` is returned, so you can chain this with other method calls.
        """
        self.singular = value
        return self

    def set_formatting_options(self, value: Optional[UrlFormattingOptions]) -> Url:
        """Does  `self.formatting_options = value` for you while returning `self`.
        `self` is returned, so you can easily chain this with other method calls if you wish.
        """
        self.formatting_options = value
        return self

    def append_url(self, url: Optional[UrlStr]) -> Url:
        """Takes the components of url, and any that look true [ie: are not False or None]
        are set on myself.

        In the case of the path, `append_path` is called instead, so the path provided in
        `url` is appended to any already existing path.

        For the query, the `append_query()` is used, and only keys with the same key-name
        will be replaced. Otherwise, the query key/value is added to any already existing
        query key/value pairs.

        For methods, `append_methods` is called, and will add any methods not already present.

        `self` is returned, so you can chain this with other method calls.
        """
        if url is None:
            return self

        # Make sure we have a Url, we want to look at it's various components...
        url = Url.ensure_url(url, default_formatting_options=self.formatting_options)

        self.append_path(url.path)
        self.append_query(url._query)
        self.append_methods(url._methods)
        self.append_metadata(url._metadata)

        for attr_name in _attributes_to_set_when_appending:
            other_value = getattr(url, attr_name, None)
            if other_value is not None:
                setattr(self, attr_name, other_value)

        return self

    def append_metadata(self, value: dict | None):
        """ Merge all dict values passed in into internal metadata dict,
            setting the value inside self for every key in provided dict.

            Any metadata keys on self that are not in passed in value dict will be left as-is.

            A shallow copy will be made of value, ie: `copy(value)` before it's added to self.

            `self` is returned, so you can chain this with other method calls.

            If `None` is passed in, does nothing.
        """
        if value is None:
            return self

        metadata = self._metadata
        if metadata is None:
            metadata = {}
            self._metadata = metadata

        for k, v in value.items():
            metadata[k] = copy(v)

        return self

    def append_path(self, path_component: Optional[str]) -> Url:
        """Appends path with path_component, making sure to add a slash if needed to separate
        new component from any current path.

        `self` is returned, so you can chain this with other method calls.
        """
        if not path_component:
            return self

        path_component = str(path_component)
        if not path_component:
            return self

        # Remove any starting slash if needed, we will be providing our own slash later.
        if path_component[0] == '/':
            path_component = path_component[1:]

        current_path = self._path

        if not current_path:
            current_path = ''

        # If the current path ends in a slash, remove it.
        if len(current_path) > 0 and current_path[-1] == '/':
            current_path = current_path[:-1]

        # Append the new path component with a slash to separate it.
        self._path = f'{current_path}/{path_component}'
        self._path_changed()
        return self

    def append_query(self, query: Optional[Query]) -> Url:
        """Calls `Url.query_add` for each key/value pair in query. Only keys with the
        same key-name will be replaced. Otherwise, the query key/value is added to any already
        existing query key/value pairs.

        `self` is returned, so you can chain this with other method calls.
        """
        if not query:
            return self

        for key, value in query.items():
            self.query_add(key, value)
        return self

    def append_methods(self, methods: Iterable[str]) -> Url:
        if methods:
            self._methods.update(methods)
        return self

    def methods_add(self, method: str) -> Url:
        if method:
            self._methods.add(method)
        return self

    def methods_remove(self, method: str) -> Url:
        if method:
            self._methods.discard(method)
        return self

    # ---------------------------------
    # --------- Query Methods ---------

    def query_add(self, key: str = None, value: QueryValue = None) -> Url:
        """Use to set a key in query easily. This will entirely replace query with name `key`
        if the value is not None. If value is None, nothing will happen/change.
        If you want to remove a query item, use 'self.query_remove(...)' instead.

        A query value can be either a str/int, or a list of str/int.
        If it is a list, then see self.formatting_options for details on what happens.

        A shallow copy will be made of value, ie: `copy(value)` before it's added to url.

        `self` is returned, so you can chain this with other method calls.
        """

        if value is None:
            return self

        if self._query is None:
            self._query = {}

        self._query[key] = copy(value)
        return self

    def query_remove(self, key) -> Url:
        """Remove value for key in query, if key does not exist nothing happens.
        `self` is returned, so you can chain this with other method calls.
        """
        self._query.pop(key, None)
        return self

    def query_value(self, key: str) -> Optional[QueryValue]:
        """ Returns the value in query assigned to key, if key not found returns `None`. """
        return self._query.get(key, None)

    # -----------------------------------------------------------------
    # --------- Dict Access into Query Values Special Methods ---------

    def __setitem__(self, key, item):
        self.query_add(key, item)

    def __getitem__(self, key):
        return self.query_value(key)

    def __len__(self):
        v = self._query
        if not v:
            return 0
        return len(v)

    def __delitem__(self, key):
        self.query_remove(key)

    def __bool__(self):
        # Check to see if `url` is empty in terms of any url string it would generate.
        return bool(str(self))

    # ---------------------------
    # --------- Private ---------

    def _copy_from_url(self, url: Url):
        """Correctly copies in an optimized way, everything in url into self."""
        self.__dict__.update(url.__dict__)
        self._query = copy(url._query)
        self._methods = copy(url._methods)
        self._cached_format_keys = copy(url._cached_format_keys)
        self._metadata = copy(url._metadata)

    def _set_query(self, query: Query):
        """Makes _query the same as query, filter out None values and making a first-level deep
        copy of the dict. This is needed in case we have lists of strings as a value.
        """
        if query is None:
            query = {}

        # Filter out None values from dictionary.
        self._query = {k: copy(v) for k, v in query.items() if v is not None}

    def _set_methods(self, methods: Union[Iterable[str], str]):
        if methods is None:
            methods = tuple()

        if isinstance(methods, str):
            methods = (methods,)

        self._methods = set(methods)

    def _path_changed(self):
        """ Called when path changes, mainly to reset format_keys cache. """
        self._cached_format_keys = None

    def _format_keys(self) -> List[str]:
        """Returns a list of format keys that are in the path. It caches this information
        lazily. Be sure to call `Url._path_changed()` when the path changes, which throws away
        this cached info.
        """
        keys = self._cached_format_keys
        if keys is not None:
            return keys

        path = self.path
        if path:
            keys = [t[1] for t in string.Formatter().parse(path) if t[1] is not None]
        else:
            keys = []

        self._cached_format_keys = keys
        return keys

    def _parse_string_into_query(self, query_string: str) -> Query:
        """Go through each query value and parse it according to the self.formatting_options.
        Keeps single-values as non-list items.  If there is more than one value for a
        particular query key-name, it will put all the values into a list.
        """
        query = {}

        formatting = self.formatting_options or DefaultQueryValueListFormat
        delimiter = formatting.list_value_delimiter
        suffix = formatting.list_key_suffix
        suffix_len = len(suffix)
        check_formatting = True if delimiter else False

        for k, v in urlparser.parse_qs(query_string).items():
            k: str
            v: List[str]

            all_values = []
            force_list = False
            is_list_keep_suffix = False

            if check_formatting:
                for keep_suffix in (formatting.list_key_suffixes_to_keep or []):
                    if k.endswith(keep_suffix):
                        is_list_keep_suffix = True
                        break

            if check_formatting and (is_list_keep_suffix or k.endswith(suffix)):
                # If we do have something like `__in=a`, we want to keep it as a list
                # even if it only has a single item.  That way when we construct the url
                # again in the future, the `__in=a` will be preserved.
                force_list = True
                if not is_list_keep_suffix:
                    k = k[:-suffix_len]

                for item in v:
                    all_values.extend(item.split(delimiter))
            else:
                all_values.extend(v)

            existing_value = query.get(k)
            if existing_value:
                all_values.extend(xloop(existing_value))

            if force_list or len(all_values) > 1:
                query[k] = all_values
            else:
                query[k] = all_values[0]

        return query

    def _format_query_into_string(self, query: Query) -> str:
        if not query:
            return ""

        options = self.formatting_options or DefaultQueryValueListFormat
        query_filtered = {}
        for key, val in query.items():
            values = list(xloop(val))

            if not values:
                continue

            # TODO: Probably remove this, seem strange.
            formatter = values[0]
            if not isinstance(formatter, _FormattedQueryValue):
                formatter = _default_query_formatter

            formatted_query = formatter.url_query(
                key=key, url=self, url_options=options, values=values
            )
            query_filtered.update(formatted_query)

        # It's legal to have query-values contain commas and so we declare them safe.
        # This prevents them from being encoded (easier to read Url, makes them smaller).
        return urlparser.urlencode(query_filtered, doseq=True, safe=',')

    def _formatted_map(
        self, secondary_values: SecondaryValues = Default, query_keys_used: List[str] = None
    ) -> Optional[dict]:
        """

        Args:
            secondary_values: Right now this method will return None [ie: invalid url]
                if we have more than one
                object passed into this. In the future, I want to support formatting placeholders
                that support multiple objects. It's just not needed right now. But the interface
                allows for it in the future, when we get around to support it.

                If left as `xsentinels.Default` then we will use self.secondary_values,
                if any are there. You can 'attach' secondary values to a Url via:

                >>> Url.is_valid(secondary_values={'id': 2}, attach_values=True)

                If `None`, then no secondary values will be used.

            query_keys_used: List will be modified (if provided) with keys we used for placeholders
                from the query-part of the url. Normally, you would remove the query-params
                we used for this purpose before producing the final url.
        Returns:
            A dict/map of formatted query key/values.
        """
        keys = self._format_keys()
        if query_keys_used is None:
            query_keys_used = []

        if not keys:
            return {}

        if secondary_values is Default:
            secondary_values = self._secondary_values

        format_map = {}
        query = self._query
        for k in keys:
            query_value = query.get(k)

            # TODO:  ********
            # TODO:  ******** Look for a single item in query_value, and if so use that?!?
            # TODO:  ********

            if not isinstance(query_value, str):
                query_value = list(xloop(query_value))

                if len(query_value) == 1:
                    query_value = query_value[0]

            # We consider blank-strings same as 'None' for our purposes here.
            if not query_value and isinstance(query_value, str):
                query_value = None

            if query_value is not None and not isinstance(query_value, list):
                # todo: convert any dates via .isoformat() ?
                format_map[k] = str(query_value)
                query_keys_used.append(k)
                continue

            if secondary_values:
                if hasattr(secondary_values, k):
                    obj_value = getattr(secondary_values, k)
                elif isinstance(secondary_values, dict):
                    obj_value = secondary_values.get(k)
                else:
                    all_objs = list(xloop(secondary_values))
                    if len(all_objs) == 1 and hasattr(all_objs[0], k):
                        obj_value = getattr(all_objs[0], k)
                    else:
                        obj_value = None

                if obj_value is not None and not isinstance(obj_value, list):
                    format_map[k] = str(obj_value)
                    continue

            return None

        return format_map

    def _formatted_path(
        self, secondary_values: Union[object, dict] = None, query_keys_used: List[str] = None
    ) -> Optional[str]:
        """
        Formats my path and returns that. If the path could not be formatted returns False.
        If this returns False it means a missing or invalid value for the formatting key-name.

        A valid value is a str or int; NOT a list.

        In the future, I'll support dates and auto-convert them into a string. But for right
        now the value must be an int or str.
        Args:
            secondary_values: If passed in, and self.query does not have a valid value, will check
                to see
                if attribute with same format-key-name exists as an attribute on this object
                or a key if it's a dict. If the value is NOT a list, it will be used. Otherwise,
                it will be ignored as an invalid value.

            query_keys_used: If you pass in a list, and I use a query as a value for
                formatting the path, I will
                put the key of each query I use inside this list.  Normally you would not output
                the query anymore [since it's inside the path now], but you can do whatever you
                want with them.

        Returns:
            String if we have a valid path, otherwise False if we can't generate Path due to
            lack of values in `Url.query` or `secondary_values`.
        """

        mapped_values = self._formatted_map(
            secondary_values=secondary_values, query_keys_used=query_keys_used
        )

        if mapped_values is None:
            # We were unable to find values for one ore more format placeholders for our url path.
            return None

        # Url encode/quote all the values into a new dict.
        mapped_values = {k: urlparser.quote(v, safe='') for (k, v) in mapped_values.items()}
        path = self._path or ''
        if mapped_values:
            return path.format_map(mapped_values)

        return path

    _formatting_options: Optional[UrlFormattingOptions] = None
    """
        If the value is `None`, it means we use DefaultQueryValueListFormat when constructing the
        url.

        BUT it also means we DON'T append this value into another Url via `Url.append_url(...)`,
        we don't want to let this value ever override another value when appending Url's.
    """

    _singular: Optional[bool] = None
    _scheme: Optional[str] = None
    _username: Optional[str] = None
    _password: Optional[str] = None
    _host: Optional[str] = None
    _port: Optional[int] = None
    _path: Optional[str] = None
    _fragment: Optional[str] = None

    # These are always set by init method, to ensure that they are never `None`.
    _query: Query
    _methods: Set[str]

    # Others
    _cached_format_keys: Optional[List[str]] = None

    _secondary_values: SecondaryValues = None


UrlStr = Url | str | None
""" A type that can be either a string or Url.
"""


# Basically, we have to set every attribute except query/path/methods.
# For path we can append to the end of it.
# For query, we can merge them together since they are Dict's.
# For methods, we can merge them since they are lists.
_attributes_to_set_when_appending = {
    'scheme',
    'username',
    'password',
    'host',
    'port',
    'fragment',
    'singular',
    'formatting_options',
}
