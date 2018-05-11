(function() {
  var a = window.CustomEvent;
  if (!a || typeof a == "object") {
    a = function d(i, g) {
      g = g || {};
      var h = document.createEvent("CustomEvent");
      h.initCustomEvent(i, !!g.bubbles, !!g.cancelable, g.detail || null);
      return h
    };
    a.prototype = window.Event.prototype
  }

  function f(g) {
    while (g) {
      if (g.nodeName.toUpperCase() == "DIALOG") {
        return (g)
      }
      g = g.parentElement
    }
    return null
  }

  function c(g, j) {
    for (var h = 0; h < g.length; ++h) {
      if (g[h] == j) {
        return true
      }
    }
    return false
  }

  function b(g) {
    this.dialog_ = g;
    this.replacedStyleTop_ = false;
    this.openAsModal_ = false;
    g.show = this.show.bind(this);
    g.showModal = this.showModal.bind(this);
    g.close = this.close.bind(this);
    if (!("returnValue" in g)) {
      g.returnValue = ""
    }
    this.maybeHideModal = this.maybeHideModal.bind(this);
    if ("MutationObserver" in window) {
      var h = new MutationObserver(this.maybeHideModal);
      h.observe(g, {
        attributes: true,
        attributeFilter: ["open"]
      })
    } else {
      g.addEventListener("DOMAttrModified", this.maybeHideModal)
    }
    Object.defineProperty(g, "open", {
      set: this.setOpen.bind(this),
      get: g.hasAttribute.bind(g, "open")
    });
    this.backdrop_ = document.createElement("div");
    this.backdrop_.className = "backdrop";
    this.backdropClick_ = this.backdropClick_.bind(this)
  }
  b.prototype = {
    get dialog() {
      return this.dialog_
    },
    maybeHideModal: function() {
      if (!this.openAsModal_) {
        return
      }
      if (this.dialog_.hasAttribute("open") && document.body.contains(this.dialog_)) {
        return
      }
      this.openAsModal_ = false;
      this.dialog_.style.zIndex = "";
      if (this.replacedStyleTop_) {
        this.dialog_.style.top = "";
        this.replacedStyleTop_ = false
      }
      this.backdrop_.removeEventListener("click", this.backdropClick_);
      if (this.backdrop_.parentElement) {
        this.backdrop_.parentElement.removeChild(this.backdrop_)
      }
      e.dm.removeDialog(this)
    },
    setOpen: function(g) {
      if (g) {
        this.dialog_.hasAttribute("open") || this.dialog_.setAttribute("open", "")
      } else {
        this.dialog_.removeAttribute("open");
        this.maybeHideModal()
      }
    },
    backdropClick_: function(g) {
      var h = document.createEvent("MouseEvents");
      h.initMouseEvent(g.type, g.bubbles, g.cancelable, window, g.detail, g.screenX, g.screenY, g.clientX, g.clientY, g.ctrlKey, g.altKey, g.shiftKey, g.metaKey, g.button, g.relatedTarget);
      this.dialog_.dispatchEvent(h);
      g.stopPropagation()
    },
    updateZIndex: function(g, h) {
      this.backdrop_.style.zIndex = g;
      this.dialog_.style.zIndex = h
    },
    show: function() {
      this.setOpen(true)
    },
    showModal: function() {
      if (this.dialog_.hasAttribute("open")) {
        throw "Failed to execute 'showModal' on dialog: The element is already open, and therefore cannot be opened modally."
      }
      if (!document.body.contains(this.dialog_)) {
        throw "Failed to execute 'showModal' on dialog: The element is not in a Document."
      }
      if (!e.dm.pushDialog(this)) {
        throw "Failed to execute 'showModal' on dialog: There are too many open modal dialogs."
      }
      this.show();
      this.openAsModal_ = true;
      if (e.needsCentering(this.dialog_)) {
        e.reposition(this.dialog_);
        this.replacedStyleTop_ = true
      } else {
        this.replacedStyleTop_ = false
      }
      this.backdrop_.addEventListener("click", this.backdropClick_);
      this.dialog_.parentNode.insertBefore(this.backdrop_, this.dialog_.nextSibling);
      var i = this.dialog_.querySelector("[autofocus]:not([disabled])");
      if (!i) {
        var g = ["button", "input", "keygen", "select", "textarea"];
        var h = g.map(function(j) {
          return j + ":not([disabled])"
        }).join(", ");
        i = this.dialog_.querySelector(h)
      }
      document.activeElement && document.activeElement.blur && document.activeElement.blur();
      i && i.focus()
    },
    close: function(h) {
      if (!this.dialog_.hasAttribute("open")) {
        throw "Failed to execute 'close' on dialog: The element does not have an 'open' attribute, and therefore cannot be closed."
      }
      this.setOpen(false);
      if (h !== undefined) {
        this.dialog_.returnValue = h
      }
      var g = new a("close", {
        bubbles: false,
        cancelable: false
      });
      this.dialog_.dispatchEvent(g)
    }
  };
  var e = {};
  e.reposition = function(g) {
    var i = document.body.scrollTop || document.documentElement.scrollTop;
    var h = i + (window.innerHeight - g.offsetHeight) / 2;
    g.style.top = Math.max(i, h) + "px"
  };
  e.isInlinePositionSetByStylesheet = function(k) {
    for (var l = 0; l < document.styleSheets.length; ++l) {
      var q = document.styleSheets[l];
      var n = null;
      try {
        n = q.cssRules
      } catch (m) {}
      if (!n) {
        continue
      }
      for (var h = 0; h < n.length; ++h) {
        var p = n[h];
        var r = null;
        try {
          r = document.querySelectorAll(p.selectorText)
        } catch (m) {}
        if (!r || !c(r, k)) {
          continue
        }
        var g = p.style.getPropertyValue("top");
        var o = p.style.getPropertyValue("bottom");
        if ((g && g != "auto") || (o && o != "auto")) {
          return true
        }
      }
    }
    return false
  };
  e.needsCentering = function(h) {
    var g = window.getComputedStyle(h);
    if (g.position != "absolute") {
      return false
    }
    if ((h.style.top != "auto" && h.style.top != "") || (h.style.bottom != "auto" && h.style.bottom != "")) {
      return false
    }
    return !e.isInlinePositionSetByStylesheet(h)
  };
  e.forceRegisterDialog = function(g) {
    if (g.showModal) {
      console.warn("This browser already supports <dialog>, the polyfill may not work correctly", g)
    }
    if (g.nodeName.toUpperCase() != "DIALOG") {
      throw "Failed to register dialog: The element is not a dialog."
    }
    new b((g))
  };
  e.registerDialog = function(g) {
    if (g.showModal) {
      console.warn("Can't upgrade <dialog>: already supported", g)
    } else {
      e.forceRegisterDialog(g)
    }
  };
  e.DialogManager = function() {
    this.pendingDialogStack = [];
    this.overlay = document.createElement("div");
    this.overlay.className = "_dialog_overlay";
    this.overlay.addEventListener("click", function(g) {
      g.stopPropagation()
    });
    this.handleKey_ = this.handleKey_.bind(this);
    this.handleFocus_ = this.handleFocus_.bind(this);
    this.handleRemove_ = this.handleRemove_.bind(this);
    this.zIndexLow_ = 100000;
    this.zIndexHigh_ = 100000 + 150
  };
  e.DialogManager.prototype.topDialogElement = function() {
    if (this.pendingDialogStack.length) {
      var g = this.pendingDialogStack[this.pendingDialogStack.length - 1];
      return g.dialog
    }
    return null
  };
  e.DialogManager.prototype.blockDocument = function() {
    document.body.appendChild(this.overlay);
    document.body.addEventListener("focus", this.handleFocus_, true);
    document.addEventListener("keydown", this.handleKey_);
    document.addEventListener("DOMNodeRemoved", this.handleRemove_)
  };
  e.DialogManager.prototype.unblockDocument = function() {
    document.body.removeChild(this.overlay);
    document.body.removeEventListener("focus", this.handleFocus_, true);
    document.removeEventListener("keydown", this.handleKey_);
    document.removeEventListener("DOMNodeRemoved", this.handleRemove_)
  };
  e.DialogManager.prototype.updateStacking = function() {
    var h = this.zIndexLow_;
    for (var g = 0; g < this.pendingDialogStack.length; g++) {
      if (g == this.pendingDialogStack.length - 1) {
        this.overlay.style.zIndex = h++
      }
      this.pendingDialogStack[g].updateZIndex(h++, h++)
    }
  };
  e.DialogManager.prototype.handleFocus_ = function(h) {
    var g = f((h.target));
    if (g != this.topDialogElement()) {
      h.preventDefault();
      h.stopPropagation();
      h.target.blur();
      return false
    }
  };
  e.DialogManager.prototype.handleKey_ = function(i) {
    if (i.keyCode == 27) {
      i.preventDefault();
      i.stopPropagation();
      var h = new a("cancel", {
        bubbles: false,
        cancelable: true
      });
      var g = this.topDialogElement();
      if (g.dispatchEvent(h)) {
        g.close()
      }
    }
  };
  e.DialogManager.prototype.handleRemove_ = function(h) {
    if (h.target.nodeName.toUpperCase() != "DIALOG") {
      return
    }
    var g = (h.target);
    if (!g.open) {
      return
    }
    this.pendingDialogStack.some(function(i) {
      if (i.dialog == g) {
        i.maybeHideModal();
        return true
      }
    })
  };
  e.DialogManager.prototype.pushDialog = function(g) {
    var h = (this.zIndexHigh_ - this.zIndexLow_) / 2 - 1;
    if (this.pendingDialogStack.length >= h) {
      return false
    }
    this.pendingDialogStack.push(g);
    if (this.pendingDialogStack.length == 1) {
      this.blockDocument()
    }
    this.updateStacking();
    return true
  };
  e.DialogManager.prototype.removeDialog = function(h) {
    var g = this.pendingDialogStack.indexOf(h);
    if (g == -1) {
      return
    }
    this.pendingDialogStack.splice(g, 1);
    this.updateStacking();
    if (this.pendingDialogStack.length == 0) {
      this.unblockDocument()
    }
  };
  e.dm = new e.DialogManager();
  document.addEventListener("submit", function(k) {
    var l = k.target;
    if (!l || !l.hasAttribute("method")) {
      return
    }
    if (l.getAttribute("method").toLowerCase() != "dialog") {
      return
    }
    k.preventDefault();
    var i = f((k.target));
    if (!i) {
      return
    }
    var j;
    var g = [document.activeElement, k.explicitOriginalTarget];
    var h = ["BUTTON", "INPUT"];
    g.some(function(m) {
      if (m && m.form == k.target && h.indexOf(m.nodeName.toUpperCase()) != -1) {
        j = m.value;
        return true
      }
    });
    i.close(j)
  }, true);
  window.dialogPolyfill = e;
  e.forceRegisterDialog = e.forceRegisterDialog;
  e.registerDialog = e.registerDialog
})();