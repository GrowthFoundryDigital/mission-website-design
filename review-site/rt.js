// Minimal runtime for exported design boards: fills {{ holes }} from the board's
// component, wires on* handlers and refs, and re-applies values on setState.
(function () {
  var HOLE = /\{\{\s*([\w$]+)\s*\}\}/g;
  var WHOLE = /^\s*\{\{\s*([\w$]+)\s*\}\}\s*$/;
  var HAS = /\{\{\s*[\w$]+\s*\}\}/;
  var pending = false, apply = null;

  function str(v) { return v == null || v === false ? '' : String(v); }

  function DCLogic(props) { this.props = props || {}; this.state = {}; }
  DCLogic.prototype.setState = function (s) {
    var next = typeof s === 'function' ? s(this.state, this.props) : s;
    this.state = Object.assign({}, this.state, next);
    if (!pending && apply) { pending = true; requestAnimationFrame(function () { pending = false; apply(); }); }
  };
  DCLogic.prototype.forceUpdate = function () { this.setState({}); };
  window.DCLogic = DCLogic;

  window.DC = {
    boot: function (Component) {
      var root = document.getElementById('dc-root');
      root.appendChild(document.getElementById('dc-tpl').content.cloneNode(true));
      var props = {};
      try { props = JSON.parse(document.getElementById('dc-props').textContent) || {}; } catch (e) {}
      delete props.$preview;
      Object.keys(props).forEach(function (k) {
        var p = props[k];
        if (p && typeof p === 'object' && 'default' in p) props[k] = p.default;
      });
      var comp = new Component(props);
      if (!comp.props || !Object.keys(comp.props).length) comp.props = props;

      var binds = [];
      var walker = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT);
      var n;
      while ((n = walker.nextNode())) {
        if (n.nodeType === 3) {
          if (HAS.test(n.nodeValue)) binds.push({ t: 'text', n: n, tpl: n.nodeValue });
          continue;
        }
        Array.prototype.slice.call(n.attributes).forEach(function (a) {
          if (!HAS.test(a.value)) return;
          var m = a.value.match(WHOLE);
          if (m && /^on[a-z]+$/.test(a.name)) {
            binds.push({ t: 'ev', n: n, ev: a.name.slice(2), key: m[1] });
            n.removeAttribute(a.name);
          } else if (m && a.name === 'ref') {
            binds.push({ t: 'ref', n: n, key: m[1] });
            n.removeAttribute(a.name);
          } else {
            binds.push({ t: 'attr', n: n, name: a.name, tpl: a.value });
          }
        });
      }

      apply = function () {
        var vals = comp.renderVals ? comp.renderVals() : {};
        binds.forEach(function (b) {
          if (b.t === 'text') {
            var tv = b.tpl.replace(HOLE, function (_, k) { return str(vals[k]); });
            if (b.n.nodeValue !== tv) b.n.nodeValue = tv;
          } else if (b.t === 'attr') {
            var av = b.tpl.replace(HOLE, function (_, k) { return str(vals[k]); });
            if (b.n.getAttribute(b.name) !== av) b.n.setAttribute(b.name, av);
          } else if (b.t === 'ev') {
            b.fn = vals[b.key];
            if (!b.on) {
              b.on = true;
              b.n.addEventListener(b.ev, function (e) { if (typeof b.fn === 'function') b.fn(e); });
            }
          } else if (b.t === 'ref' && !b.done) {
            b.done = true;
            if (typeof vals[b.key] === 'function') vals[b.key](b.n);
          }
        });
      };
      apply();
      if (comp.componentDidMount) comp.componentDidMount();
      window.addEventListener('pagehide', function () {
        if (comp.componentWillUnmount) comp.componentWillUnmount();
      });
    }
  };
})();
