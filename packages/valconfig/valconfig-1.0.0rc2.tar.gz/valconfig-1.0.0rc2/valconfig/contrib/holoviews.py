import re
from pathlib import Path
from typing import Optional, ClassVar, Union, Literal, List
from collections.abc import Mapping, Sequence
from configparser import ConfigParser

# from mackelab_toolbox.utils import Singleton
from ..v1 import ValConfig

# Matplotlib
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    class plt:
        class style:
            available = []
            @staticmethod
            def use(s): return None

# HoloConfig
from typing import Any, Dict, Tuple
import addict
try:
    from pydantic.v1 import validator, root_validator #, StrictInt, StrictFloat, StrictBool
except ModuleNotFoundError:
    from pydantic import validator, root_validator #, StrictInt, StrictFloat, StrictBool
try:
    import holoviews as hv
except ModuleNotFoundError:
    hv = None

# Generic parameter type for Holoviews options
HoloParam = Union[int, float, bool,
                  Tuple[Union[int, float, bool], ...],
                  str]
try:
    from pydantic.v1.validators import int_validator, float_validator, bool_validator
except ModuleNotFoundError:
    from pydantic.validators import int_validator, float_validator, bool_validator
class GenericParam:

    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        """Generic validator for config file values.

        ConfigParser does not perform any validation: every value is read in as a
        string. The idea of `GenericParam` is to provide a mechanism to allow
        automatic validation of new types. Essentially we want to be able to write

        .. code::python
           class MyConfig(ValidatingConfig):
             class figures:
               cmap: holoviews.Palette
               steps: range

        and define the values in the config file as

        .. code::
           [figures]
           cmap: "viridis"
           steps: (1, 10, 2)

        without having to specify custom validators for `Palette` or `range`.

        This works by a combination of two features:

        - Recognition of simple argument types.
          A hard-coded list of simple argument types are recognized
          by inspecting the values for characteristic markers. These are:
          int, float, string, tuple, list and bool.
          For example, a value starting with '(' is recognized as a tuple, a value
          of `true` as a bool, etc.
          If a value is not recognized, it is kept as a string and stripped
          of initial and trailing whitespace.

        - Once values have been converted to string to (number/tuple/etc.),
          they are passed to type for initialization. So in the example above, this
          would result in the following initialization calls:
          ``holoviews.Palette("viridis")`` and ``range(1, 10, 2)``.

        Adding the following code to your class will apply this function to all
        types (or at least most) fields which don't have validators

        .. code::
            class MyConfig(ValidatingConfig):
              class Config:
                arbitrary_types_allowed = True

              @validator("*", pre=True)
              def apply_generic_validators(cls, val, field):
                target_type = field.type_
                if (not hasattr(target_type, "__get_validators__")  # Basic test
                    and "Union" not in str(target_type)             # Exclude complex types
                    and not isinstance(val, target_type)):          # Skip if value is already of desired type
                  val = generic_validate(target_type, val)
                return val
        """
        try:
            if isinstance(v, str):
                v = v.strip()

                # If `v` is empty, the best we can do is guess an appropriate value
                # Empty string and `None` are likely the most reasonable ones; we return None
                # (Therefore to get an empty string, the value should be "")
                if len(v) == 0:
                    return None

                # Check for special values
                if v == "<None>":
                    return None

                # Match an expression like Palette("copper")
                m = re.fullmatch(r"Palette\((['\"])([^\1]*)\1\)", v)
                if m:
                    if hv is None:
                        return v  # If HoloViews is not loaded, we can’t create a Palette
                    try:
                        pal = hv.Palette(m[2])
                    except KeyError:  # Can happen if name is mistyped, or the required backend is not loaded.
                        return v      # In particular, in headless operations where we won’t be plotting anything, 
                    else:             # we might not load any backend so we don’t want to raise an exception
                        return pal
                    return hv.Palette(m[2])
                # Match an expression like Cycle("copper")
                m = re.fullmatch(r"Cycle\((['\"])([^\1]*)\1\)", v)
                if m:
                    if hv is None:
                        return v  # If HoloViews is not loaded, we can’t create a Cycle
                    try:
                        cyc = hv.Cycle(m[2])
                    except KeyError:  # Idem
                        return v
                    else:
                        return cyc

                # Check if v is a quoted string – either "…" or '…'
                # CAUTION: This won't catch malformed expressions like ""a" – the returned value would be '"a'
                if v.startswith('"') or v.endswith('"'):
                    if not v.startswith('"') and v.endswith('"'):
                        raise ValueError("Unclosed quotations")
                    return v[1:-1]
                if v.startswith("'") or v.endswith("'"):
                    if not v.startswith("'") and v.endswith("'"):
                        raise ValueError("Unclosed quotations")
                    return v[1:-1]

                # Check if v is a tuple
                if v.startswith("(") or v.endswith(")"):
                    if not v.startswith("(") and v.endswith(")"):
                        raise ValueError("Unclosed brackets")
                    return tuple(cls.validate(item.strip())
                                 for item in v[1:-1].split(","))

                # Check if v is a list
                if v.startswith("[") or v.endswith("]"):
                    if not v.startswith("[") and v.endswith("]"):
                        raise ValueError("Unclosed brackets")
                    # Special case: empty list
                    if "," not in v and len(v[1:-1].strip() ) == 0:
                        return []
                    # Normal case
                    else:
                        return list(cls.validate(item.strip())
                                     for item in v[1:-1].split(","))

                # Check if v is a number:
                if v[0] in set("0123456789"):
                    vs = v
                    if "." in vs and "," in vs: # Format: 123,456.78  – Not recommended, because 123,456 would be converted to 123.456
                        vs = vs.replace(",", "")
                    elif "," in vs:  # Format: 123,78  – Convert to 123.78
                        vs = vs.replace(",", ".")
                    if vs.count(".") > 1:
                        raise TypeError(f"Number {v} contains more than one decimal indicator")
                    if "." in vs:
                        return float_validator(vs)
                    else:
                        return int_validator(vs)

                # Check if v is bool:
                if v.lower() in {"true", "false"}:
                    return bool_validator(v)

                # If nothing matches, return a string
                return v
            else:
                # If not a string, leave it as is.
                # However, still recurse into tuples / lists to validate their content
                if isinstance(v, (tuple, list)):
                    return type(v)(cls.validate(item) for item in v)
                else:
                    return v

        except (ValueError, TypeError, AssertionError) as e:
            # To help debugging, we add a message to errors which are caught by Pydantic
            raise type(e)(f"Error occurred while validating {cls}") from e


def generic_validate(target_type, value):
    return target_type(GenericParam.validate(value))

# class DictModel(BaseModel):
#     "Used to parse dictionaries exported as JSON"
#     class Config:
#         extra = "allow"

# class _HoloConfigCreator(metaclass=Singleton):
#     def __init__(self):
#         self.config_types = {}
#     def __getitem__(self, backend):
#         try:
#             return self.config_types[backend]
#         except KeyError:
#             self.config_types[backend] = type(
#                 f"HoloConfig[{backend}]", (HoloConfigBase,), {"_backend": backend})
#             return self.config_types[backend]
# HoloConfig = _HoloConfigCreator()

def make_addict(obj: Mapping) -> addict.Dict:
    d = addict.Dict(obj.items())
    for k, v in d.items():
        if isinstance(v, Mapping):
            d[k] = make_addict(v)
    return d

def split_cycles(d: dict) -> dict:
    for k, v in d.items():
        if k.lower() == "cycle" and isinstance(v, str):
            d[k] = v.split()
        elif isinstance(v, dict):
            d[k] = split_cycles(v)
    return d

def _replace_colors(value, colors):
    # NB: This function is called for all fields, not just colors, so it needs
    #     to correctly ignore non-color values
    if isinstance(value, str) and value.startswith("colors."):
        c = colors
        for field in value.split(".")[1:]:
            c = c.get(field)
        # Check if color is a cycle
        if isinstance(c, (list, tuple)) and hv:  # Color cycle
            name = value[7:]  # Remove 'colors.'
            return hv.Cycle(name, values=c)
        else:
            return c
    elif isinstance(value, dict):
        for k, v in value.items():
            value[k] = _replace_colors(v, colors)
        return value
    else:
        return value

class HoloConfigBase(ValConfig):
    _elem_names = {"Curve", "Scatter", "Overlay", "Layout", "Area"}
    _backend: ClassVar[str]

    # NB: Resolving relative paths only works for config files
    colors: Union[Path, dict] = Path(__file__).parent/"paul_tol_colors.cfg"
    defaults: Dict[str, GenericParam]={}

    Area   : Dict[str, GenericParam]={}
    Curve  : Dict[str, GenericParam]={}
    Layout : Dict[str, GenericParam]={}
    Overlay: Dict[str, GenericParam]={}
    Scatter: Dict[str, GenericParam]={}
    # TODO: Add all hv Elements

    renderer: Dict[str, Any]={}

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **kwargs):
        """Extend `values` dict to include the capitalized forms used by HoloViews

        Example:
            {'curve': {'width': 200}}
        becomes
            {'curve': {'width': 200}, 'Curve': {'width': 200}}
        """
        elem_names = {field.name.lower(): field.name
                      for field in self.__fields__.values()}
                      # if field.name in self._elem_names}
        cap_vals = {}
        for option, value in kwargs.items():
            cap_name = elem_names.get(option.lower())
            if cap_name and cap_name not in cap_vals:
                cap_vals[cap_name] = value
        kwargs.update(cap_vals)
        super().__init__(**kwargs)

    # _prepend_rootdir = validator("colors", allow_reuse=True)(prepend_rootdir)

    @validator("*", pre=True)
    def apply_generic_validators(cls, val, field):
        target_type = field.type_
        if ( not hasattr(target_type, "__get_validators__")  # Basic test
             and all(s not in str(target_type)
                     for s in ("Union", "Any", "[")) ):      # Exclude complex types
            try:
                # Skip if value is already of desired type
                is_target_type = isinstance(val, target_type)
            except TypeError:
                # If we missed a complex type we might end up here
                pass
            else:
                if not is_target_type:
                    val = generic_validate(target_type, val)
        return val

    @validator("defaults", *_elem_names)
    def make_attribute_dict(cls, val, field):
        if isinstance(val, dict):
            val = make_addict(val)
        # All config objects should explicitely specify 'backend'.
        # This avoids an issue where using the `.opts` method to further specify options unsets previous options
        val["backend"] = val.get("backend", cls._backend)
        return val

    # @validator("*", pre=True)
    # def parse_element_options(cls, opts, field):
    #     """Support passing multiple values as a dictionary
        
    #     As a convenience, and to allow greater concision, plot options can be
    #     specified as a dictionary:
        
    #         [figures.matplotlib]
    #         Curve = {linewidth: 3, color: blue}

    #     which is equivalent to

    #         [figures.matplotlib.Curve]
    #         linewidth = 3
    #         color = blue

    #     Missing quotes are automatically inserted: ``{key: val}  ->  {'key': 'val'}``,
    #     but only if there are no quotes in option value.
    #     So ``{'key': val}`` would be left unchanged.
    #     `val` is wrapped iff it start with a letter or underscore.
    #     """
    #     if isinstance(opts, str) and opts.strip().startswith("{"):
    #         if not {"'", '"'}.intersection(opts):
    #             # If there are no quotes at all
    #             raw = re.sub(r"([{,])\s*(\w+)\s*:", r'\1 "\2":', opts)
    #             raw = re.sub(r":\s*([a-zA-Z_]+\w*)\s*([,}])", r': "\1" \2', raw)
    #         return DictModel.parse_raw(raw).__dict__  # FIXME: Use Pydantic’s dict validator directly
    #     else:
    #         return opts

    @validator("colors")
    def load_colors(cls, colors):
        if isinstance(colors, Path):
            # NB: This validators runs before the `prepend_rootdir` from ValConfig,
            #     so we need to resolve the path ourselves
            colors = cls.resolve_path(colors)
            colorcfg = ConfigParser()
            with open(colors) as f:
                colorcfg.read_file(f)
            colors = colorcfg
        if isinstance(colors, ConfigParser):
            # Convert to a dict
            colordict = make_addict(colorcfg)
            colordict.pop("DEFAULT", None)
            colors = colordict
        return colors

    @validator("colors")
    def convert_to_addict(cls, colors):
        return make_addict(colors)

    @validator("colors")
    def split_color_cycles(cls, colors):
        return split_cycles(colors)

    @validator("*")
    def replace_colors(cls, val, values):
        """
        Replace entries like `colors.pale.yellow` with the corresponding 
        value from the `colors` field.
        """
        colors = values.get("colors")
        if colors is not None:
            return _replace_colors(val, colors)
        else:
            return val

    @property
    def all_element_opts(self):
        """Return all set opts, for all plot Elements, including defaults."""
        if not hv:  # If HoloViews is not installed, then there are no allowed opts
            return {}
        allowed_opts = hv.opts._element_keywords(self._backend, self._elem_names)
        opts = {}
        for elem in self._elem_names:
            # List of default attributes we defined and which are applicable to this element
            opts[elem] = {}
            if getattr(self, "defaults"):
                opts[elem].update({k:v for k,v in self.defaults.items()
                                   if k in allowed_opts[elem]})
            elem_opts = getattr(self, elem, None)
            if elem_opts:
                opts[elem].update(elem_opts)
        return opts

class HoloMPLConfig(HoloConfigBase):
    """
    Adds a `style` field, which should be an argument compatible with :py:func:`pyplot.style.use()`.
    These parameters are automatically set as defaults figure parameters:
    whenever the field `style` is changed, `plt.style.use()` is executed with the new value.
    """
    _backend = "matplotlib"
    style: Optional[Union[List[Union[str, Path]], Union[str,Path]]] = None

    class Config:
        validate_assignment: True  # Re-trigger plt.style.use when we assign to `style`

    @validator("style", pre=True)
    def path_or_str(cls, style_file):
        """
        Keep `style_file` as a string if it matches an entry in plt.style.available,
        otherwise convert to a Path.
        """
        style_file = GenericParam.validate(style_file)  # `apply_generic_validators` is called after this validator, because it is assigned with "*"
        if isinstance(style_file, str):
            if style_file not in plt.style.available:
                style_file = cls.resolve_path(style_file)
            return style_file
        elif isinstance(style_file, Sequence):
            return [cls.path_or_str(name) for name in style_file]
        else:
            return style_file

    @validator("style")
    def update_plot_style(cls, style_file):
        if style_file:
            plt.style.use(style_file)
        return style_file


class HoloBokehConfig(HoloConfigBase):
    _backend = "bokeh"

class FiguresConfig(ValConfig):

    backend: Literal["matplotlib", "bokeh"]
    matplotlib: Optional[HoloMPLConfig] = None
    bokeh: Optional[HoloBokehConfig]    = None

    class Config:
        arbitrary_types_allowed = True

    @root_validator(pre=True)
    def preload_backends(cls, values):
        """
        A number of Holoviews actions (like retrieving a color palette or
        setting options) are only possible after a backend has been loaded.
        By loading backends preemptively, we allow these actions to be done
        within validators like GenericParam.validate
        We do this in two separate steps: 
        - In this pre-validator, we load the renderers with default options.
        - In the post-validator below, once the values have been pa   we check if they contain arguments for the renderer and set them.
        """
        try:
            import holoviews as hv
        except ModuleNotFoundError:
            return values  # If holoviews is not installed, there’s nothing to do
        if values.get("matplotlib"):
            hv.renderer("matplotlib")
        if values.get("bokeh"):
            hv.renderer("bokeh")
        return values

    @root_validator
    def set_renderer_args(cls, values):
        """By preemptively loading the backends, we ensure that e.g.
        ``hv.opts(*config.figures.bokeh)`` does not raise an exception.
        """
        if hv is None:  # Nothing to do if Holoviews is not installed
            return values
        if values.get("matplotlib"):
            renderer = hv.renderer("matplotlib")
            render_args = values["matplotlib"].renderer
            if render_args:
                for kw, val in render_args.items():
                    setattr(renderer, kw, val)

        if values.get("bokeh"):
            renderer = hv.renderer("bokeh")
            render_args = values["bokeh"].renderer
            if render_args:
                for kw, val in render_args.items():
                    setattr(renderer, kw, val)

        return values

    @root_validator
    def set_defaults(cls, values):
        if hv is None:  # Nothing to do if Holoviews is not installed
            return values
        for backend in ["matplotlib", "bokeh"]:
            if values.get(backend) and backend in hv.Store.renderers:  # If backend is not in `renderers`, than the best guess is that `load_backends` failed for that backend
                hv.Store.set_current_backend(backend)  # Only to silence warnings
                hv.opts.defaults(values[backend].all_element_opts)
        hv.Store.set_current_backend(values.get("backend"))
        return values

    @validator("*", pre=True)
    def apply_generic_validators(cls, val, field):
        target_type = field.type_
        if ( not hasattr(target_type, "__get_validators__")  # Basic test
             and any(s not in str(target_type)
                     for s in ("Union", "Any", "[")) ):      # Exclude complex types
            try:
                # Skip if value is already of desired type
                is_target_type = isinstance(val, target_type)
            except TypeError:
                # If we missed a complex type we might end up here
                pass
            else:
                if not is_target_type:
                    val = generic_validate(target_type, val)
        return val

    def __getattr__(self, attr):
        "Use the config associated to `backend` as default."
        return getattr(getattr(self, self.backend), attr)
